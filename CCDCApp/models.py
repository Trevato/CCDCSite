# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActionRecorder(models.Model):
    module = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255)
    success = models.CharField(max_length=1, blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'action_recorder'


class AddressBook(models.Model):
    address_book_id = models.AutoField(primary_key=True)
    customers_id = models.IntegerField()
    entry_gender = models.CharField(max_length=1, blank=True, null=True)
    entry_company = models.CharField(max_length=255, blank=True, null=True)
    entry_firstname = models.CharField(max_length=255)
    entry_lastname = models.CharField(max_length=255)
    entry_street_address = models.CharField(max_length=255)
    entry_suburb = models.CharField(max_length=255, blank=True, null=True)
    entry_postcode = models.CharField(max_length=255)
    entry_city = models.CharField(max_length=255)
    entry_state = models.CharField(max_length=255, blank=True, null=True)
    entry_country_id = models.IntegerField()
    entry_zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address_book'


class AddressFormat(models.Model):
    address_format_id = models.AutoField(primary_key=True)
    address_format = models.CharField(max_length=128)
    address_summary = models.CharField(max_length=48)

    class Meta:
        managed = False
        db_table = 'address_format'


class Administrators(models.Model):
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'administrators'


class Banners(models.Model):
    banners_id = models.AutoField(primary_key=True)
    banners_title = models.CharField(max_length=64)
    banners_url = models.CharField(max_length=255)
    banners_image = models.CharField(max_length=64)
    banners_group = models.CharField(max_length=10)
    banners_html_text = models.TextField(blank=True, null=True)
    expires_impressions = models.IntegerField(blank=True, null=True)
    expires_date = models.DateTimeField(blank=True, null=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_status_change = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banners'


class BannersHistory(models.Model):
    banners_history_id = models.AutoField(primary_key=True)
    banners_id = models.IntegerField()
    banners_shown = models.IntegerField()
    banners_clicked = models.IntegerField()
    banners_history_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banners_history'


class Categories(models.Model):
    categories_id = models.AutoField(primary_key=True)
    categories_image = models.CharField(max_length=64, blank=True, null=True)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoriesDescription(models.Model):
    categories_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    categories_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'categories_description'
        unique_together = (('categories_id', 'language_id'),)


class Configuration(models.Model):
    configuration_id = models.AutoField(primary_key=True)
    configuration_title = models.CharField(max_length=255)
    configuration_key = models.CharField(max_length=255)
    configuration_value = models.TextField()
    configuration_description = models.CharField(max_length=255)
    configuration_group_id = models.IntegerField()
    sort_order = models.IntegerField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()
    use_function = models.CharField(max_length=255, blank=True, null=True)
    set_function = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuration'


class ConfigurationGroup(models.Model):
    configuration_group_id = models.AutoField(primary_key=True)
    configuration_group_title = models.CharField(max_length=64)
    configuration_group_description = models.CharField(max_length=255)
    sort_order = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuration_group'


class Counter(models.Model):
    startdate = models.CharField(max_length=8, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counter'


class CounterHistory(models.Model):
    month = models.CharField(max_length=8, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counter_history'


class Countries(models.Model):
    countries_id = models.AutoField(primary_key=True)
    countries_name = models.CharField(max_length=255)
    countries_iso_code_2 = models.CharField(max_length=2)
    countries_iso_code_3 = models.CharField(max_length=3)
    address_format_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    currencies_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12, blank=True, null=True)
    symbol_right = models.CharField(max_length=12, blank=True, null=True)
    decimal_point = models.CharField(max_length=1, blank=True, null=True)
    thousands_point = models.CharField(max_length=1, blank=True, null=True)
    decimal_places = models.CharField(max_length=1, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class Customers(models.Model):
    customers_id = models.AutoField(primary_key=True)
    customers_gender = models.CharField(max_length=1, blank=True, null=True)
    customers_firstname = models.CharField(max_length=255)
    customers_lastname = models.CharField(max_length=255)
    customers_dob = models.DateTimeField()
    customers_email_address = models.CharField(max_length=255)
    customers_default_address_id = models.IntegerField(blank=True, null=True)
    customers_telephone = models.CharField(max_length=255)
    customers_fax = models.CharField(max_length=255, blank=True, null=True)
    customers_password = models.CharField(max_length=60)
    customers_newsletter = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class CustomersBasket(models.Model):
    customers_basket_id = models.AutoField(primary_key=True)
    customers_id = models.IntegerField()
    products_id = models.TextField()
    customers_basket_quantity = models.IntegerField()
    final_price = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    customers_basket_date_added = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers_basket'


class CustomersBasketAttributes(models.Model):
    customers_basket_attributes_id = models.AutoField(primary_key=True)
    customers_id = models.IntegerField()
    products_id = models.TextField()
    products_options_id = models.IntegerField()
    products_options_value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customers_basket_attributes'


class CustomersInfo(models.Model):
    customers_info_id = models.IntegerField(primary_key=True)
    customers_info_date_of_last_logon = models.DateTimeField(blank=True, null=True)
    customers_info_number_of_logons = models.IntegerField(blank=True, null=True)
    customers_info_date_account_created = models.DateTimeField(blank=True, null=True)
    customers_info_date_account_last_modified = models.DateTimeField(blank=True, null=True)
    global_product_notifications = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers_info'


class GeoZones(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    geo_zone_name = models.CharField(max_length=32)
    geo_zone_description = models.CharField(max_length=255)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'geo_zones'


class Languages(models.Model):
    languages_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=2)
    image = models.CharField(max_length=64, blank=True, null=True)
    directory = models.CharField(max_length=32, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Manufacturers(models.Model):
    manufacturers_id = models.AutoField(primary_key=True)
    manufacturers_name = models.CharField(max_length=32)
    manufacturers_image = models.CharField(max_length=64, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturers'


class ManufacturersInfo(models.Model):
    manufacturers_id = models.IntegerField(primary_key=True)
    languages_id = models.IntegerField()
    manufacturers_url = models.CharField(max_length=255)
    url_clicked = models.IntegerField()
    date_last_click = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturers_info'
        unique_together = (('manufacturers_id', 'languages_id'),)


class Newsletters(models.Model):
    newsletters_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    module = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletters'


class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    customers_id = models.IntegerField()
    customers_name = models.CharField(max_length=255)
    customers_company = models.CharField(max_length=255, blank=True, null=True)
    customers_street_address = models.CharField(max_length=255)
    customers_suburb = models.CharField(max_length=255, blank=True, null=True)
    customers_city = models.CharField(max_length=255)
    customers_postcode = models.CharField(max_length=255)
    customers_state = models.CharField(max_length=255, blank=True, null=True)
    customers_country = models.CharField(max_length=255)
    customers_telephone = models.CharField(max_length=255)
    customers_email_address = models.CharField(max_length=255)
    customers_address_format_id = models.IntegerField()
    delivery_name = models.CharField(max_length=255)
    delivery_company = models.CharField(max_length=255, blank=True, null=True)
    delivery_street_address = models.CharField(max_length=255)
    delivery_suburb = models.CharField(max_length=255, blank=True, null=True)
    delivery_city = models.CharField(max_length=255)
    delivery_postcode = models.CharField(max_length=255)
    delivery_state = models.CharField(max_length=255, blank=True, null=True)
    delivery_country = models.CharField(max_length=255)
    delivery_address_format_id = models.IntegerField()
    billing_name = models.CharField(max_length=255)
    billing_company = models.CharField(max_length=255, blank=True, null=True)
    billing_street_address = models.CharField(max_length=255)
    billing_suburb = models.CharField(max_length=255, blank=True, null=True)
    billing_city = models.CharField(max_length=255)
    billing_postcode = models.CharField(max_length=255)
    billing_state = models.CharField(max_length=255, blank=True, null=True)
    billing_country = models.CharField(max_length=255)
    billing_address_format_id = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    cc_type = models.CharField(max_length=20, blank=True, null=True)
    cc_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_number = models.CharField(max_length=32, blank=True, null=True)
    cc_expires = models.CharField(max_length=4, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_purchased = models.DateTimeField(blank=True, null=True)
    orders_status = models.IntegerField()
    orders_date_finished = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    currency_value = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersProducts(models.Model):
    orders_products_id = models.AutoField(primary_key=True)
    orders_id = models.IntegerField()
    products_id = models.IntegerField()
    products_model = models.CharField(max_length=12, blank=True, null=True)
    products_name = models.CharField(max_length=64)
    products_price = models.DecimalField(max_digits=15, decimal_places=4)
    final_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_tax = models.DecimalField(max_digits=7, decimal_places=4)
    products_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders_products'


class OrdersProductsAttributes(models.Model):
    orders_products_attributes_id = models.AutoField(primary_key=True)
    orders_id = models.IntegerField()
    orders_products_id = models.IntegerField()
    products_options = models.CharField(max_length=32)
    products_options_values = models.CharField(max_length=32)
    options_values_price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'orders_products_attributes'


class OrdersProductsDownload(models.Model):
    orders_products_download_id = models.AutoField(primary_key=True)
    orders_id = models.IntegerField()
    orders_products_id = models.IntegerField()
    orders_products_filename = models.CharField(max_length=255)
    download_maxdays = models.IntegerField()
    download_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders_products_download'


class OrdersStatus(models.Model):
    orders_status_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    orders_status_name = models.CharField(max_length=32)
    public_flag = models.IntegerField(blank=True, null=True)
    downloads_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_status'
        unique_together = (('orders_status_id', 'language_id'),)


class OrdersStatusHistory(models.Model):
    orders_status_history_id = models.AutoField(primary_key=True)
    orders_id = models.IntegerField()
    orders_status_id = models.IntegerField()
    date_added = models.DateTimeField()
    customer_notified = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_status_history'


class OrdersTotal(models.Model):
    orders_total_id = models.AutoField(primary_key=True)
    orders_id = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    class_field = models.CharField(db_column='class', max_length=32)  # Field renamed because it was a Python reserved word.
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders_total'


class Products(models.Model):
    products_id = models.AutoField(primary_key=True)
    products_quantity = models.IntegerField()
    products_model = models.CharField(max_length=12, blank=True, null=True)
    products_image = models.CharField(max_length=64, blank=True, null=True)
    products_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_date_added = models.DateTimeField()
    products_last_modified = models.DateTimeField(blank=True, null=True)
    products_date_available = models.DateTimeField(blank=True, null=True)
    products_weight = models.DecimalField(max_digits=5, decimal_places=2)
    products_status = models.IntegerField()
    products_tax_class_id = models.IntegerField()
    manufacturers_id = models.IntegerField(blank=True, null=True)
    products_ordered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class ProductsAttributes(models.Model):
    products_attributes_id = models.AutoField(primary_key=True)
    products_id = models.IntegerField()
    options_id = models.IntegerField()
    options_values_id = models.IntegerField()
    options_values_price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'products_attributes'


class ProductsAttributesDownload(models.Model):
    products_attributes_id = models.IntegerField(primary_key=True)
    products_attributes_filename = models.CharField(max_length=255)
    products_attributes_maxdays = models.IntegerField(blank=True, null=True)
    products_attributes_maxcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_attributes_download'


class ProductsDescription(models.Model):
    products_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    products_name = models.CharField(max_length=64)
    products_description = models.TextField(blank=True, null=True)
    products_url = models.CharField(max_length=255, blank=True, null=True)
    products_viewed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_description'
        unique_together = (('products_id', 'language_id'),)


class ProductsImages(models.Model):
    products_id = models.IntegerField()
    image = models.CharField(max_length=64, blank=True, null=True)
    htmlcontent = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products_images'


class ProductsNotifications(models.Model):
    products_id = models.IntegerField(primary_key=True)
    customers_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_notifications'
        unique_together = (('products_id', 'customers_id'),)


class ProductsOptions(models.Model):
    products_options_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    products_options_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'products_options'
        unique_together = (('products_options_id', 'language_id'),)


class ProductsOptionsValues(models.Model):
    products_options_values_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    products_options_values_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'products_options_values'
        unique_together = (('products_options_values_id', 'language_id'),)


class ProductsOptionsValuesToProductsOptions(models.Model):
    products_options_values_to_products_options_id = models.AutoField(primary_key=True)
    products_options_id = models.IntegerField()
    products_options_values_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products_options_values_to_products_options'


class ProductsToCategories(models.Model):
    products_id = models.IntegerField(primary_key=True)
    categories_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products_to_categories'
        unique_together = (('products_id', 'categories_id'),)


class Reviews(models.Model):
    reviews_id = models.AutoField(primary_key=True)
    products_id = models.IntegerField()
    customers_id = models.IntegerField(blank=True, null=True)
    customers_name = models.CharField(max_length=255)
    reviews_rating = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    reviews_status = models.IntegerField()
    reviews_read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reviews'


class ReviewsDescription(models.Model):
    reviews_id = models.IntegerField(primary_key=True)
    languages_id = models.IntegerField()
    reviews_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'reviews_description'
        unique_together = (('reviews_id', 'languages_id'),)


class SecDirectoryWhitelist(models.Model):
    directory = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sec_directory_whitelist'


class Sessions(models.Model):
    sesskey = models.CharField(primary_key=True, max_length=32)
    expiry = models.PositiveIntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Specials(models.Model):
    specials_id = models.AutoField(primary_key=True)
    products_id = models.IntegerField()
    specials_new_products_price = models.DecimalField(max_digits=15, decimal_places=4)
    specials_date_added = models.DateTimeField(blank=True, null=True)
    specials_last_modified = models.DateTimeField(blank=True, null=True)
    expires_date = models.DateTimeField(blank=True, null=True)
    date_status_change = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'specials'


class TaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    tax_class_title = models.CharField(max_length=32)
    tax_class_description = models.CharField(max_length=255)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_class'


class TaxRates(models.Model):
    tax_rates_id = models.AutoField(primary_key=True)
    tax_zone_id = models.IntegerField()
    tax_class_id = models.IntegerField()
    tax_priority = models.IntegerField(blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=4)
    tax_description = models.CharField(max_length=255)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_rates'


class WhosOnline(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255)
    session_id = models.CharField(max_length=128)
    ip_address = models.CharField(max_length=15)
    time_entry = models.CharField(max_length=14)
    time_last_click = models.CharField(max_length=14)
    last_page_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'whos_online'


class Zones(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_country_id = models.IntegerField()
    zone_code = models.CharField(max_length=32)
    zone_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zones'


class ZonesToGeoZones(models.Model):
    association_id = models.AutoField(primary_key=True)
    zone_country_id = models.IntegerField()
    zone_id = models.IntegerField(blank=True, null=True)
    geo_zone_id = models.IntegerField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zones_to_geo_zones'
