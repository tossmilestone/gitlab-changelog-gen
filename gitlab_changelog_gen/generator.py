import gitlab

class ChangeLogGenerator(object):
    MAIN_TEMPLATE='''# CHANGELOG

{releases}'''
    RELEASE_TEMPLATE=\
'''## Release {milestone}
{changes}'''
    CHANGE_TEMPLATE='''
### Features
{features}
### Bug Fixes
{bugs}
'''
    CHANGE_ITEM_TEMPLATE='''* {title} ({ref}, {author})'''

    def __init__(self, host, group, project, user=None, password=None, private_token=None, output='CHANGELOG.md'):
        self.host = host
        self.user = user
        self.password = password
        self.private_token = private_token
        self.group = group
        self.project = project
        self.output = output

    @classmethod
    def from_config(cls, config, output='CHANGELOG.md'):
        return ChangeLogGenerator(
            host = config.host,
            private_token = config.private_token,
            group = config.group,
            project = config.project,
            output = output,
        )

    def generate(self):
        c = gitlab.Gitlab(self.host, email=self.user, password=self.password, private_token=self.private_token)
        pl = c.projects.list(search=self.project)
        if not pl:
            print("Project %s not found" % self.project)
            return
        p = None
        for pp in pl:
            if pp.namespace['name'] == self.group:
                p = pp
                break
        if not p:
            print("Project in group %s not found" % self.group)
            return

        mts = p.milestones.list()
        mts = sorted(mts, key=lambda x: x.created_at, reverse=True)
        mts_changes = [{'milestone': m, 'changes': {'features': [], 'bugs': []}} for m in mts]
        mts_map = {m['milestone'].id : m for m in mts_changes}
        mrs = p.mergerequests.list(state='merged', query_parameters={'per_page':1000000000}, order_by='created_at', sort='asc')
        for m in mrs:
            if m.milestone and m.milestone['id'] in mts_map:
                changes = mts_map[m.milestone['id']]['changes']
                if 'feature' in m.labels or 'enhancement' in m.labels:
                    changes['features'].append(m)
                elif 'bug' in m.labels:
                    changes['bugs'].append(m)

        release_tpl = []
        for mc in mts_changes:
            # Render features
            feats = self.gen_change_item(mc['changes']['features'])
            # Render bugs
            bugs = self.gen_change_item(mc['changes']['bugs'])
            change_tpl = self.CHANGE_TEMPLATE.format(
                features='\n'.join(feats),
                bugs='\n'.join(bugs)
            )
            release_tpl.append(self.RELEASE_TEMPLATE.format(
                milestone=mc['milestone'].title,
                changes=change_tpl,
            ))
        changelog = self.MAIN_TEMPLATE.format(releases='\n'.join(release_tpl))
        with open(self.output, 'w+') as out:
            out.write(changelog)
            print("Changelog is generated to '%s' success." % self.output)

    def gen_change_item(self, changes):
        changes_tpl = []
        for c in changes:
            changes_tpl.append(
                self.CHANGE_ITEM_TEMPLATE.format(
                    title=c.title,
                    ref='[%s](%s)' % (c.reference, c.web_url),
                    author='[%s](%s)' % (c.author['username'], c.author['web_url'])
                )
            )
        return changes_tpl
