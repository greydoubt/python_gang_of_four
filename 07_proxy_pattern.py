'''demonstrates the Proxy pattern, which provides a surrogate or placeholder for another object to control access to it. In this example, Subject is the interface for both the RealSubject and Proxy classes. RealSubject represents the real object that Proxy is a placeholder for. The request method is overridden by both classes, but Proxy overrides it to add its own functionality before or after calling the RealSubject's request method.'''

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        return f"Proxy({self._real_subject.request()})"

# Usage:
real_subject = RealSubject()
proxy = Proxy(real_subject)

print(real_subject.request())
print(proxy.request())
