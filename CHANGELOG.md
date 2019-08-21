# CHANGELOG
## Release ACP 2.2

### Features
* Support resource search case insensitive ([!61](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/61), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Refactor request attribute getter ([!57](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/57), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Support application import/export resources ([!51](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/51), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Add list application all resources ([!49](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/49), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Enh/remove unuse code ([!47](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/47), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add Batch create Resource ([!46](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/46), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add create GeneralNamespace Api ([!45](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/45), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add application creator user ([!44](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/44), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Add application create failed condition ([!43](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/43), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Modified CronJob Exec Method Get->Post ([!41](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/41), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add Swagger params Modified CronJob Exec URL ([!38](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/38), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add Pod Logs Api ([!32](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/32), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Refactor code to add unit test ([!27](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/27), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
### Bug Fixes
* Fix pvc match any workload ([!60](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/60), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Fix service match any application ([!59](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/59), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Return k8s errors directly ([!58](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/58), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix incorrect coverage value ([!56](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/56), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix no coverage on gitlab ci ([!55](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/55), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix applicaiton status update error ([!54](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/54), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix application status override ([!53](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/53), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix jenkinsfile error ([!52](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/52), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix App address is null ([!50](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/50), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Fix api log url namespace->namespaces ([!48](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/48), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Cherry pick branch 'fix/app-resource-ownerref' into 'master' ([!42](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/42), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Cherry pick branch 'fix/delete-field-fail-on-update-app' into 'master' ([!36](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/36), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Cherry pick branch 'fix/delete-field-fail-on-update-app' into 'master' ([!35](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/35), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Clear root CAData if insecure flag is true ([!30](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/30), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Search resource returns 200 ([!29](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/29), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix search resource with gzip encoding ([!28](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/28), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))

## Release ACP 2.1

### Features
* Add get resourcestype api and Add cronjob exec ([!26](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/26), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Add topology api ([!19](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/19), [yjai](https://gitlab.aks.myalauda.cn/yjai))
* Support OPTIONS request ([!16](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/16), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Add resource search API ([!13](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/13), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Change archon chart name ([!12](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/12), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
### Bug Fixes
* Fix missing app resource owner ref ([!39](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/39), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix orphan pods on app deploy deleted ([!34](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/34), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix update app resources failed ([!33](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/33), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Clear root CAData if insecure flag is true ([!31](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/31), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix list app history forbidden ([!25](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/25), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix search resource error ([!24](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/24), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix app update fail ([!23](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/23), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix POST without BODY 406 ([!22](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/22), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix inconsistent apiVersion on k8s API access ([!21](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/21), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix component kinds resolve error msg ([!20](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/20), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Use CORS filter ([!18](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/18), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix wrong options allow headers ([!17](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/17), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* Fix rollback error ([!15](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/15), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* [no-jira]fix json marshal empty slice as null ([!14](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/14), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))
* [DEV-19385]Fix missing address when setup multiple alb2 ([!10](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/10), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))

## Release ACP 2.0

### Features
* [ACP-93]Feat/alb2 addr ([!6](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/6), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))
* Add jenkins file ([!4](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/4), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
### Bug Fixes
* fix DEV-19385 ([!11](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/11), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))
* Fix ingress-nginx no addr ([!8](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/8), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))
* Merge branch 'feat/alb2-addr' into 'master' ([!7](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/7), [hexiaoxi](https://gitlab.aks.myalauda.cn/hexiaoxi))
* [ACP-139]fix no address ([!5](https://gitlab.aks.myalauda.cn/alauda/archon/merge_requests/5), [yanzhu](https://gitlab.aks.myalauda.cn/yanzhu))
