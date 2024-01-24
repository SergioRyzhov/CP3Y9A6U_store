from django.db import models


class CreditOrder(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.id)


class Contract(models.Model):
    number = models.PositiveIntegerField(
        max_length=255,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    credit_order = models.OneToOneField(
        CreditOrder,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='credit_order',
    )

    def __str__(self):
        return f"{str(self.id)} {str(self.number)}"


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


class Good(models.Model):
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
        related_name='credit_order',
    )

    manufacturer = models.OneToOneField(
        Manufacturer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='manufacturer',
    )

    def __str__(self):
        return f"{str(self.id)} {self.name}"
