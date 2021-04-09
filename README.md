# DjangoTaskProject_Model_django-framework_Migrate_sqlite_to_mysql

DjangoTaskProject_Model_django-framework_Migrate_sqlite_to_mysql

..\tareas-test\tareasproject2

[test]

python manage.py runserver

  http://127.0.0.1:8000/

administration panel :

http://localhost:8000/admin/

[1][export data]

python manage.py dumpdata > datadump.json

[2][install/check mysqlclient]

[2.1]  (run : mysql)

Create DB in MYSQL : sqlite3tomysql

[2.2][setup db mysql]

..\tareas-test\tareasproject2\tareasproject

DATABASES = {

    'sqlite': {
    
        'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': BASE_DIR / 'db.sqlite3',
        
    },
    
    'default': {
    
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'sqlite3tomysql',
        
        'USER': 'root',
        
        'PASSWORD': '',
        
        'HOST': 'localhost',
        
        'PORT': '3306',
        
        'OPTIONS': {
        
            'sql_mode': 'traditional',
            
        }
        
    }
    
}

[3]

manage.py makemigrations

manage.py migrate

[4]

python manage.py loaddata datadump.json

[All OK][!!!]


[test in mysql]

python manage.py runserver

  http://127.0.0.1:8000/

administration panel :

http://localhost:8000/admin/

Add a new Task

& watch it in MySQL


Table : tareas_tarea	

TASK8

SELECT * FROM `tareas_tarea` WHERE nombre = 'TASK8';

TASK8

TASK #8

2

2021-04-07 19:11:07.205750
