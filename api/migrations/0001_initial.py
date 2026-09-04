from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="User", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("username", models.CharField(max_length=100, unique=True)),
        ]),
        migrations.CreateModel(name="Driver", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100)),
            ("latitude", models.FloatField(default=17.385)),
            ("longitude", models.FloatField(default=78.4867)),
            ("available", models.BooleanField(default=True)),
        ]),
        migrations.CreateModel(name="Ride", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("pickup", models.CharField(max_length=200)),
            ("destination", models.CharField(max_length=200)),
            ("status", models.CharField(default="requested", max_length=30)),
            ("fare", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ("driver", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="api.driver")),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.user")),
        ]),
        migrations.CreateModel(name="Notification", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("message", models.CharField(max_length=255)),
            ("read", models.BooleanField(default=False)),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.user")),
        ]),
    ]
