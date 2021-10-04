# Q4-Capstone

#### **How To Get Started**

To start you need to make sure and download django. I used pip to install. Then you will need to make sure you have poetry installed and set up the virtual environments. 

1. Make sure to clone in terminal.
```bash
git clone
```

2. Make sure to install the dependencies in terminal.
```bash
poetry install
```

3. Activate the Virtual Environment.
```bash
poetry shell
```

4. Make sure to migrate!
```bash
python manage.py migrate
```

5. Create your superuser. 
```bash
python manage.py createsuperuser
```

6. Finally run the server to watch the magic unfold.
```bash
python manage.py runserver
```