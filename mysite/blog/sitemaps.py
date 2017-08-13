'''
Sitemap are XML files that tell search engines the pages
of your website, their relevance, and how frequently they are updated. By using a
sitemap, we will help crawlers indexing your website's content.
'''

from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.9

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.publish
