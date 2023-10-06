from django.contrib import admin
from .models import event_team_reg, customer_register, Login

# Register your models here.
# from .models import event_team_reg
admin.site.register(event_team_reg)

# from .models import customer_register
admin.site.register(customer_register)

# from .models import Login
admin.site.register(Login)


