from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number, gender, is_admin, password=None):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            gender=gender,
            is_admin=is_admin,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(max_length=70, upload_to='accounts/static/img/user', null=True, default=None)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    gender = models.CharField(choices=((1, 'masculin'), (2, 'feminin')), max_length=8)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'gender', 'password']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def name(self):
        return f'{self.first_name} {self.last_name}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    product = models.ForeignKey('product.Product', on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.quantity)


class ProductBought(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    product = models.ForeignKey('product.Product', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.product}'
