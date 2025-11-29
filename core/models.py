from django.core.files.base import ContentFile
from django.db import models
from django.db.models.functions import Coalesce
from django.db.models import Sum, F
import math
import decimal
from django.db.models import Sum, Subquery, F, OuterRef, DecimalField, Value, IntegerField, Max

import uuid
from urllib.parse import urlparse
import os
import os.path
import random
from django.conf import settings
from django.core.files import File

