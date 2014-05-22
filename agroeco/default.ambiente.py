# coding=utf-8
from iampacks.cross.ambiente.models import BaseAmbiente
import os

site_id = None

class Ambiente(BaseAmbiente):
  productivo=False

  site_id=site_id

  dominio='dev.%s'%site_id
  puerto_http='80'
  puerto_https='443'

  admins = (
    ('admin', 'mail@mail.com'),
  )

  class db:
    name=site_id
    user=site_id
    password=None

  project_directory = '%s/' % os.path.abspath('%s/..' % os.path.split(os.path.abspath(__file__))[0])
  wsgi_dir = os.path.dirname(__file__)

  class email:
    host = 'localhost'
    user = 'user@domain'
    password = None
    port = 587

  class zonomi:
    api_key = None

  class backup:
    user = 'cerebro'
    host = 'test.iamsoft'
    destination = 'backups/%s' % site_id

ambiente=Ambiente()

