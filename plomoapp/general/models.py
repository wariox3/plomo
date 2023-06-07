from django.db import models

class Ciudad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = "gen_ciudad"
        
class Contacto(models.Model):        
    numero_identificacion = models.CharField(max_length=20)
    nombre_corto = models.CharField(max_length=200)  
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "gen_contacto"

