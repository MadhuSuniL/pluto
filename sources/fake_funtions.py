from faker.providers import BaseProvider
import random

class Provider(BaseProvider):
    def ipv4_address(self):
        octets = [str(self.random_int(min=0, max=255)) for _ in range(4)]
        return ".".join(octets)

    def ipv6_address(self):
        hextets = [format(self.random_int(min=0, max=65535), "x") for _ in range(8)]
        return ":".join(hextets)
    
    def aadhaar_card_number(self):
        aadhaar_number = self.random_int(min=1000_0000_0000, max=9999_9999_9999)
        return f"{aadhaar_number}"

from faker import Faker
fake = Faker()
fake.add_provider(Provider)


def generate_fake_value(attr):
    res = ''
    data_type = attr.replace('_', ' ').title()
    value = getattr(fake,attr)
    fake_value = value()
    patterns = [
    f"Sure, here's some fake data for <b>{data_type}</b>: <b>{fake_value}</b>.",
    f"I can generate a fake value for <b>{data_type}</b>. How about this: <b>{fake_value}</b>.",
    f"Here's a fake <b>{data_type}</b>: <b>{fake_value}</b>.",
    f"Need a fake <b>{data_type}</b>? I've got you covered: <b>{fake_value}</b>.",
    f"I can generate a fake <b>{data_type}</b> for you. How about this: <b>{fake_value}</b>.",
    f"Looking for a fake <b>{data_type}</b>? Try this: <b>{fake_value}</b>.",
    f"I can generate fake <b>{data_type}</b> values. Here's one: <b>{fake_value}</b>.",
    f"Sure, here's a fake <b>{data_type}</b> for you: <b>{fake_value}</b>.",
    f"How about this fake <b>{data_type}</b>? <b>{fake_value}</b>.",
    f"This is a fake <b>{data_type}</b>: <b>{fake_value}</b>.",
    f"Looking for a fake <b>{data_type}</b>? I've got you covered with this: <b>{fake_value}</b>.",
    f"Here's a fake <b>{data_type}</b> for you: <b>{fake_value}</b>.",
    f"Need a fake <b>{data_type}</b>? Try this one: <b>{fake_value}</b>.",
    f"This is a fake <b>{data_type}</b> value: <b>{fake_value}</b>.",
    f"How about a fake <b>{data_type}</b>? Check this out: <b>{fake_value}</b>.",
    f"Sure, here's a fake <b>{data_type}</b>: <b>{fake_value}</b>.",
    f"Need a fake <b>{data_type}</b>? No problem, try this one: <b>{fake_value}</b>.",
    f"I can generate a fake <b>{data_type}</b> for you. Here's one: <b>{fake_value}</b>.",
    f"Here's a fake <b>{data_type}</b> value: <b>{fake_value}</b>.",
    f"Looking for a fake <b>{data_type}</b>? This should do the trick: <b>{fake_value}</b>.",
    f"How about a fake <b>{data_type}</b>? Check out this one: <b>{fake_value}</b>.",
    f"Here's a fake <b>{data_type}</b> for you to use: <b>{fake_value}</b>.",
    f"I can generate fake <b>{data_type}</b> values. How about this one: <b>{fake_value}</b>.",
    f"Need a fake <b>{data_type}</b>? Try this one: <b>{fake_value}</b>.",
    f"Looking for a fake <b>{data_type}</b>? Here's one: <b>{fake_value}</b>.",
    f"This is a fake <b>{data_type}</b> that should work: <b>{fake_value}</b>.",
    f"Want a fake <b>{data_type}</b>? Check this out: <b>{fake_value}</b>",
    f"I've got a fake {data_type} value for you: {fake_value}.",
    f"Need a fake {data_type}? No problem, here you go: {fake_value}.",
    f"This is a fake {data_type}: {fake_value}."
    ]
    res += random.choice(patterns)+'<br>'    
    return [res,fake_value] 

# print(generate_fake_value('address'))
    
    