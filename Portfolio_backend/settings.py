from pathlib import Path
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_qa)twradqm+i0=7a%)s@m!y7bckh!2=y!+njo4ph#l6t+#%tc'

DEBUG = True

ALLOWED_HOSTS = ["*"]  # or set your backend domain once deployed

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",       # For local React dev
    "https://portfolio-react-js-ashen.vercel.app",  # Your deployed Vercel frontend
]



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Portfolio_App',
    'Portfolio_Admin_App',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'Portfolio_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portfolio_backend.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "PortFolio Admin",
    "site_header": "PortFolio Admin",
    "site_brand": "PortFolio Admin",
    # "site_logo": "books/img/logo.png",
    "login_logo": "PortFolio Admin",
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the Portfolio Admin",
    "copyright": "Library Ltd",
    "search_model": ["auth.User"],  # Add models you want searchable
    "user_avatar": None,

    # Top menu links reflecting your dashboard sections
"topmenu_links": [
    {"name": "Dashboard", "url": "admin:index"},
    {"name": "Projects", "url": "admin:Portfolio_Admin_App_project_changelist"},
    {"name": "Portfolio", "url": "admin:Portfolio_Admin_App_portfolio_changelist"},
    {"name": "Experience", "url": "admin:Portfolio_Admin_App_experience_changelist"},
    {"name": "Skills", "url": "admin:Portfolio_Admin_App_skill_changelist"},
    {"name": "Contact", "url": "admin:Portfolio_Admin_App_contactmessage_changelist"},
    {"name": "About", "url": "admin:Portfolio_Admin_App_about_changelist"},
],

    # User menu links
    "usermenu_links": [
        {"model": "auth.user"},
    ],

    # Sidebar settings
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["Dashboard", "Projects", "Portfolio", "Experience", "Skills", "Contact"],
   

    # Custom links (optional, you could add quick "Add Project/Experience/Portfolio" here)
    "custom_links": {
        "books": [
            {"name": "Add Project", "url": "project_create", "icon": "fas fa-plus", "permissions": ["books.add_project"]},
            {"name": "Add Experience", "url": "experience_create", "icon": "fas fa-plus", "permissions": ["books.add_experience"]},
            {"name": "Add Portfolio", "url": "portfolio_create", "icon": "fas fa-plus", "permissions": ["books.add_portfolio"]},
        ]
    },

    # Icons for models/apps
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        "books": "fas fa-book",
        "Portfolio_Backend.Projects": "fas fa-project-diagram",
        "Portfolio_Backend.Portfolio": "fas fa-briefcase",
        "Portfolio_Backend.Experience": "fas fa-history",
        "Portfolio_Backend.Skills": "fas fa-cogs",
        "Portfolio_Backend.Contact": "fas fa-envelope",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Related modals
    "related_modal_active": False,

    # UI tweaks
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # Change view
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,
}

