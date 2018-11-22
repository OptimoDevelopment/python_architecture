1. dockerfile
2. manifests walkthrough
opowiedz czym sa:
- pody
- deployments
- svc
- ingress
wspomnij o:
- hpa
- statefullset
- volumes
- jobs/cronjobs

dzialania z manifestami
`kubectl apply -f manifests`
`kubectl delete -f manifests`
issues: multiple envs require copies... boring

3. helm
instalacja apki
`helm upgrade --install demo-app -f helm/demo-app/values.yaml --debug --dry-run helm/demo-app`

bump wersji
`helm upgrade --install demo-app -f helm/demo-app/values.yaml -f helm/env/staging.yaml --debug --dry-run helm/demo-app`

helm list

historia rewizji
`helm history demo-app`
`helm rollback demo-app 1`
`helm history demo-app`
`helm get manifest demo-app --revision 2`

4. Horizontal pod autoscaler:
`kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10`

5. locustio
`docker run --rm -v `pwd`:/locust -p 8089:8089 christianbladescb/locustio --host https://demo-app-k8s.testowaplatforma123.net`




