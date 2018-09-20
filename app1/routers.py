class App1Router(object):

	def db_for_read(self,model,**hints):

		if model._meta.app_label == 'app1':
			return 'db2'
		return None

	def db_for_write(self,model,**hints):

		if model._meta.app_label == 'app1':
			return 'db1'

		return None

	def db_relation(self,obj1,obj2, **hints):

		## this is returned true if the both objects are of same database. 
		if obj1._meta.app_label == 'app1' and obj2._meta.app_label == 'app1':
			return True
		return None

	def allow_migrate(self,db,app_label,model_name=None, **hints):

		## migration only is only for app1 in database db1
		if app_label == 'app1':
			return db=='db1'

		## migration for other apps is not accepted in db1 
		elif db == 'db1':
			return False

		return None