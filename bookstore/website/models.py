from django.db import models


class User(models.Model):

    # userID = models.CharField('User ID', max_length=10)
    first_name = models.CharField('User First Name', max_length=30)
    last_name = models.CharField('User Last Name', max_length=30)
    email = models.EmailField('User Email')
    password = models.CharField('User Password', max_length=100)
    address = models.CharField('User Address', max_length=300)
    zip_code = models.CharField('User Zip Code', max_length=15)
    phone = models.CharField('User Phone', max_length=15)


    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.email


class Book(models.Model):

    # bookID = models.CharField('Book ID', max_length=10)
    title = models.CharField('Book Title', max_length=100)
    description = models.TextField(blank=True, max_length=1000)
    author = models.CharField('Book Author', max_length=100)
    genre = models.CharField('Book Genre/s', max_length=100)
    numPages = models.CharField('Book Number of Pages', max_length=100)
    available = models.BooleanField('Book Available')
    image = models.CharField('Book Image Path', max_length=100)
    price = models.CharField('Book Price', max_length=100)
    num_available = models.CharField('Number of Available Books', max_length=10, blank=True, null=True)


    def __str__(self):
        return (
            'Title: ' + self.title + '; Author: ' + self.author + '; Genre: ' + self.genre + 
            '; Number of pages: ' + self.numPages + '; Available: ' + str(self.available) + 
            '; Image: ' + self.image + '; Price: ' + self.price + '; Number of available books ' + str(self.num_available))

class Order(models.Model):

    # orderID = models.CharField('Order ID', max_length=10)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, blank=True)
    amount = models.CharField('Order Amount', max_length=10, blank=True, null=True,)
    date = models.DateTimeField('Order Date')
    successful = models.BooleanField('Order Successful')


    def __str__(self):
        return 'User: ' + str(self.user) + '; Amount: ' + str(self.amount) + '; Books: ' + str(self.book.all()).replace('<QuerySet', '').replace('<', '').replace('>', '') + '; Date: ' + str(self.date)


class MfgInventory(models.Model):

    
    title = models.CharField('Book Title', max_length=100)
    author = models.CharField('Book Author', max_length=100)
    genre = models.CharField('Book Genre/s', max_length=100)
    available = models.BooleanField('Book Available')
    image = models.CharField('Book Image Path', max_length=100)
    price = models.CharField('Book Price', max_length=100)
    qty_available = models.CharField('Qty in Inventory', max_length=10, blank=True, null=True)

    def __str__(self):

        return ('Title: ' + self.title + '; Author: ' + self.author + '; Genre: ' + self.genre + '; Available: ' + str(self.available) +
                '; Imgage:' + self.image + '; Price: ' + self.price + '; Qty: ' + str(self.qty_available)) 
