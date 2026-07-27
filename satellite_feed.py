# The corrupted satellite data feed
satellite_feeds = [
    "72-69-76-76-79",       # Encrypted Word 1 (ASCII decimal codes)
    "87-79-82-76-68",       # Encrypted Word 2 (ASCII decimal codes)
    42,                     # Global positioning float code (Corrupted data!)
    "  _sYstEm_oNlInE_  ",  # System status string
    "0"                     # Battery critical override multiplier
]





def decrypt(feed):

    p1 = feed[0]
    p2 = feed[1]

    split1 = p1.split ("-")
    split2 = p2.split ("-")

    
    

    message1 = "".join(chr(int(n)) for n in split1)
    message2 = "".join(chr(int(n)) for n in split2)

    return message1, message2

m1, m2 = decrypt(satellite_feeds)

print(m1)
print(m2)

def clean_up(feed):
    status = feed[3]

    status = status.strip()

    status = status.strip("_")

    status = status.lower()

    return status

cleaned_up = clean_up(satellite_feeds)

print(cleaned_up)



# This fails when it tries to run the number 42 in the sateliite feed
# def decode_words(feed):
 #   parts = feed.split("-")
  #  return "".join(chr(int(n)) for n in parts)


# for item in satellite_feeds:
   # print(decode_words(satellite_feeds))

   def decode_words(item):
    parts = item.split("-")
    return "".join(chr(int(n)) for n in parts)

for item in satellite_feed:
    try:
        # Try to decode every item
        decoded = decode_words(item)
        print(decoded)

        # Try dividing 100 by the 5th item ("0")
        result = 100 / int(satellite_feed[4])
        print(result)

    except AttributeError:
        print("[SYSTEM WARNING]: Skipped corrupted non-string data.")

    except ZeroDivisionError:
        print("[SYSTEM WARNING]: Cannot divide by zero override.")
