from django.db import models
from faker import Faker
from app.models import Product, Category, Section  # Import your models here

fake = Faker()


def generate_fake_products(num_products):
    for _ in range(num_products):
        product = Product(
            vendor_name=fake.company(),
            total_quantity=fake.random_int(min=1, max=1000),
            Availability=fake.random_int(min=0, max=1000),
            featured_image=fake.image_url(),
            product_name=fake.word(),
            price=fake.random_int(min=10, max=500),
            Discount=fake.random_int(min=0, max=50),
            tax=fake.random_int(min=0, max=30),
            packing_cost=fake.random_int(min=0, max=20),
            Product_Information=fake.paragraph(nb_sentences=3),
            model_name=fake.word(),
            Categories=Category.objects.order_by(
                '?').first(),  # Choose a random category
            Tags=fake.word(),
            Description=fake.paragraph(
                nb_sentences=5, variable_nb_sentences=True, ext_word_list=None),
            section=Section.objects.order_by(
                '?').first(),  # Choose a random section
            slug=fake.slug(),
        )
        product.save()


# Call the function to generate 100 fake products
generate_fake_products(100)
