import factory
import random
from decimal import Decimal
from addresses import models as addresses_models
from goods import models as goods_models
from hr import models as hr_models
from lots import models as lots_models
from stocks import models as stocks_models
from revaluation import models as revaluation_models
from crm import models as crm_models

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Country'
        django_get_or_create = ('name', )

    name = factory.Faker('country')


class RegionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Region'
        django_get_or_create = ('name', )

    parent = CountryFactory()
    name = factory.Faker('region')

class CityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.City'
        django_get_or_create = ('name', )

    parent = RegionFactory()
    name = factory.Faker('city')


class DistrictFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.District'
        django_get_or_create = ('name', )

    parent = CityFactory()
    name = factory.Faker('city')


class StreetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Street'
        django_get_or_create = ('name', )

    name = factory.Faker('street_name')
    parent = DistrictFactory()


class MakerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Maker'
        django_get_or_create = ('name', )

    name = factory.Faker('company')
    country = CountryFactory()


class TradeNameFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.TradeName'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Category'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class MeasureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = goods_models.Measure
        django_get_or_create = ('name', )

    name = factory.Faker('pyint')


class PackingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Packing'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class OriginalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Original'
        django_get_or_create = ('count', )

    count = factory.Faker('pyint')


class GoodFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Good'
        django_get_or_create = ('description', )

    name = TradeNameFactory()
    maker = MakerFactory()
    packing = PackingFactory()
    original = OriginalFactory()
    category = CategoryFactory()
    measure = MeasureFactory()
    description = factory.Faker('text')


class DepartmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'hr.Department'
        django_get_or_create = ('name', )

    name = factory.Faker('job')


class EmployeeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'hr.Employee'
        django_get_or_create = (
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'position',
            'role',
            'birthday',
        )

    department = DepartmentFactory()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = factory.Faker('middle_name')
    phone = factory.Faker('phone_number')
    position = factory.Faker('job')
    role = factory.Faker('job')
    birthday = factory.Faker('date_of_birth')


class CurrencyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'lots.Currency'
        django_get_or_create = ('name', )

    name = factory.Faker('currency_name')


class StockFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stocks.Stock'
        django_get_or_create = (
            'name',
            'house',
            )

    name = factory.Faker('word')
    country = CountryFactory()
    house = factory.Faker('building_number')
    region = RegionFactory()
    city = CityFactory()
    district= DistrictFactory()
    street = StreetFactory()


class LotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'lots.Lot'
        django_get_or_create = (
            'base_price',
            'series',
            'shelf_life',
            'quantity',
        )

    good = GoodFactory()
    base_price = Decimal('25.00')
    series = factory.Faker('upc_e')
    currency = CurrencyFactory()
    shelf_life = factory.Faker('future_date')
    quantity = factory.Faker('pyint')
    stock = StockFactory()


class RevaluationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'revaluation.Pricing'
        django_get_or_create = ('name', 'coefficient', )

    name = factory.Faker('word')
    coefficient = factory.Faker('pyfloat')


class AgreementStatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'crm.AgreementStatus'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class AgreementFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'crm.Agreement'
        django_get_or_create = ('status', 'result', )

    status = AgreementStatusFactory()
    result = random.choice([0,1,2])
