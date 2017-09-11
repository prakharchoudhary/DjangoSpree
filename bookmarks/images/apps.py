from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'
    verbose_name = 'Image Bookmarks'

    def ready(self):
    	# import signal handlers
    	import images.signals
