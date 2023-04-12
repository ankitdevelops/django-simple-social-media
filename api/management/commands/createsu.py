from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username="ankit").exists():
            User.objects.create_superuser(
                username="ankit",
                name="Ankit Kumar",
                email="ankit@gmail.com",
                password="testing321",
            )
        if not User.objects.filter(username="mohit").exists():
            User.objects.create_user(
                username="mohit",
                name="Mohit Kumar",
                email="mohit@gmail.com",
                password="testing321",
            )
        if not User.objects.filter(username="sheetal").exists():
            User.objects.create_user(
                username="sheetal",
                name="Sheetal",
                email="sheetal@gmail.com",
                password="testing321",
            )
        if not User.objects.filter(username="john").exists():
            User.objects.create_user(
                username="john",
                name="John Kumar",
                email="john@gmail.com",
                password="testing321",
            )
        if not User.objects.filter(username="manish").exists():
            User.objects.create_user(
                username="manish",
                name="Manish Kumar",
                email="manish@gmail.com",
                password="testing321",
            )

        print("Users has been created.")
