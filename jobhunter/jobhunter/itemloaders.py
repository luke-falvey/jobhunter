import unicodedata

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst

class JobAdloader(ItemLoader):
    text_in = MapCompose(str.strip)
    text_out = Join()
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()


class SeekLoader(JobAdloader):
    text_in = MapCompose(lambda unicode_str: unicodedata.normalize("NFKD", unicode_str), str.strip)

    