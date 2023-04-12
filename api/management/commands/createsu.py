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
        print("Superuser has been created.")
