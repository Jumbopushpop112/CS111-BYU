import bs4
import requests
from urllib.parse import urlparse, urljoin
import re
class RequestGuard:
    """
    Constructor
    """
    def __init__(self, url):
        self.parsed_URL = urlparse(url)
        self.domain = self.parsed_URL.netloc
        self.forbidden = self.parse_robots()
    """
    Returns a list of forbidden paths. The regex expression gets all the items after the Disallow: string
    """
    def parse_robots(self):
        robots_file = f"{self.parsed_URL.scheme}://{self.domain}/robots.txt"
        response = requests.get(robots_file)
        list_forbidden = re.findall(r"Disallow:\s*(.*)",response.text)
        return list_forbidden
    """
    Returns True if a link can be followed
    """
    def can_follow_link(self,url):
        parsed = urlparse(url)
        if parsed.netloc != self.domain:
            return False
        parsed_path = parsed.path
        for forbidden_path in self.forbidden:
            if parsed_path.startswith(forbidden_path):
                return False
        return True
    """
    This method is very simple. It checks if the link it is passed can be followed, and if it can, returns whatever requests.get() would return if passed the same arguments. If the link cannot be followed, it returns None.
    """
    def make_get_request(self, url, use_stream = False):
        if not self.can_follow_link(url):
            return None
        return requests.get(url, stream = use_stream)
