# ZJNUCloud API

Public API of ZJNUCloud App which should be deployed on the cloud server/VPS. Including:  
* News data (/news)  
* Workshops data (/speech)  
* School key dates (/keydates)  
* App top carousel data (/banner)  
* Bus (in development)    

*Note: News and workshops data come from WeChat offical and portals of ZJNU, extracted by a spider  https://github.com/zjnu/zjnucloud-spider*

云上浙师公网API接口，部署在云服务器/VPS上。包括以下模块:  
* 新闻聚合数据接口 (/news)  
* 讲座预告数据接口 (/speech)  
* 校历数据接口 (/news)  
* App首页轮播图接口 (/banner)  
* 公交信息接口 (/news)  

*注：新闻和讲座数据来自浙师大官方微信和各官方网站，爬虫脚本：  https://github.com/zjnu/zjnucloud-spider*

## Deployment

### Clone the repo  
> git clone https://github.com/ddmax/zjnucloud-api.git  

### Using Docker  
Require:  
* [Docker](https://docs.docker.com/engine/installation/) >= 1.10  
* [docker-compose](https://docs.docker.com/compose/install/) >= 1.7.0

> cd zjnucloud-api  
> docker-compose up  

### Manual installation

#### Ubuntu 14.04

1. Install dependencies  
	```bash  
	cd zjnucloud-api
	pip install -r requirements.txt
	```

2. Specify STATIC_FILES variable in settings.py, which stores all static files in production environment. For example, create a static folder in current dir and set:
	```
	STATIC_ROOT = os.path.join(BASE_DIR, "static/")
	```

	then:
	```bash
	python manage.py collectstatic
	```

3. Setup database part in settings.py, then
	```bash
	python manage.py migrate
	```

4. Write the following uWSGI configuration to zjnucloud-api.ini file:
	```
	[uwsgi]
	ini = :base
	socket = /tmp/zjnucloud-api.sock
	master = true
	pidfile=/tmp/zjnucloud-api.pid
	daemonize=/var/log/uwsgi/zjnucloud-api.log
	processes = 4
	harakiri = 30
	
	[local]
	ini = :base
	http = :8000
	
	[base]
	module=zjnucloud-api.wsgi:application
	chmod-socket=666
	```

5. Run uWSGI
	```
	uwsgi --ini zjnucloud-api.ini --touch-reload reload
	```

6. Visit http://127.0.0.1:8000. Enjoy it~

## License
	Copyright 2016 ddMax
	
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	    http://www.apache.org/licenses/LICENSE-2.0
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.