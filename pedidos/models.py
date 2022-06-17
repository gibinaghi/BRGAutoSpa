from lib2to3.refactor import get_all_fix_names
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Pedido(models.Model):  #hereda de models.Model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # devuelve el id del pedido
        return self.id

    # agrego una propiedad para obtener el total del pedido
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
        )['total']

    class Meta:
        # crear la table en la base de datos
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.cantidad} unidades de {self.producto_id.nombre})'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']