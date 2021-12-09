import re

ip4 = re.compile(r"""
    (?:(?:25[0-5]| # 250-255
          2[0-4][0-9]|  # 200-249
          [01]?[0-9]?[0-9])\.){3}
          (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])
""", re.VERBOSE)


if __name__ == "__main__": # альтернативное решение
    ip4 = re.compile(r"""
        (?:(?:1?[0-9]?[0-9]\.| # 0 - 199
        2?[0-4]?[[0-9]\.| # 200 - 249
        2?[0-5]?[[0-5]\.){3} #250 - 255
        (?:1?[0-9]?[0-9]|2?[0-4]?[[0-9]|2?[0-5]?[[0-5]))
    """, re.VERBOSE)
    pass


