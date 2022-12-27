from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager): 
    def _create_user(self, email, password, is_admin, **extra_fields):
        
        if not email:
            raise ValueError('Insira um email')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_admin=is_admin,
            **extra_fields
        )

        user.set_passsword(password)

        user.save(using=self.db)

        return user

    def create_admin(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_admin=True,
            **extra_fields
            )
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_admin=False,
            **extra_fields
        )