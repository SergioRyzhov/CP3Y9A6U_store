from django.db import models


class Contract(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{str(self.id)} {str(self.number)}"


class CreditOrder(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='contract_id',
    )

    def __str__(self):
        return f"{str(self.contract)} {str(self.created_at)}"


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{str(self.id)} {self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    credit_order = models.ForeignKey(
        CreditOrder,
        on_delete=models.CASCADE,
        related_name='orders',
    )

    manufacturer = models.OneToOneField(
        Manufacturer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='manufacturer',
    )

    def __str__(self):
        return f"{str(self.id)} {self.name}"
