import pyshorteners

def shorten_url(long_url):
    # Initialize the Shortener class
    s = pyshorteners.Shortener()

    # Shorten the long URL
    short_url = s.tinyurl.short(long_url)

    return short_url

if __name__ == "__main__":
    long_url = input("Enter the long URL to shorten: ")
    shortened_url = shorten_url(long_url)
    
    print("Shortened URL:", shortened_url)
