import time
import timeit

from article_converter import article_convert
from article_converter import article_convert_old

# Create your tests here.

start1 = time.time()
result1 = article_convert_old(
    "A top-level domain (TLD) is one of the domains at the highest level in the hierarchical Domain Name System of "
    "the Internet after the root domain. The top-level domain names are installed in the root zone of the name space. "
    "For all domains in lower levels, it is the last part of the domain name, that is, the last non empty label of a "
    "fully qualified domain name. For example, in the domain name www.example.com., the top-level domain is com. "
    "Responsibility for management of most top-level domains is delegated to specific organizations by the ICANN an "
    "Internet multi-stakeholder community, which operates the Internet Assigned Numbers Authority (IANA), "
    "and is in charge of maintaining the DNS root zone.")

stop1 = time.time()

start2 = time.time()
result2 = article_convert(
    "A top-level domain (TLD) is one of the domains at the highest level in the hierarchical Domain Name System of "
    "the Internet after the root domain. The top-level domain names are installed in the root zone of the name space. "
    "For all domains in lower levels, it is the last part of the domain name, that is, the last non empty label of a "
    "fully qualified domain name. For example, in the domain name www.example.com., the top-level domain is com. "
    "Responsibility for management of most top-level domains is delegated to specific organizations by the ICANN an "
    "Internet multi-stakeholder community, which operates the Internet Assigned Numbers Authority (IANA), "
    "and is in charge of maintaining the DNS root zone.")

stop2 = time.time()

print(start1)
print(f"article_convert took {stop1 - start1} seconds")
print(f"article_convert_old took {stop2 - start2} seconds")
print(f"article_convert was {(stop1 - start1) / (stop2 - start2)} faster")

print(result1 == result2)
