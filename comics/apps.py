from __future__ import unicode_literals

from django.apps import AppConfig

class ComicsConfig(AppConfig):
	name = 'comics'

	def ready(self):
		import comics.signals
