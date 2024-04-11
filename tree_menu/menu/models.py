from django.db import models


class Menu(models.Model):
    """Model Menu."""
    name = models.CharField(max_length=150, verbose_name="Название меню")
    parent = models.ForeignKey(
        to="self",
        related_name="children",
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Родительское меню"
        )
