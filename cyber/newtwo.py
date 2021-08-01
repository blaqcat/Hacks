valid_ip = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

        valid_host = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"

        vp = re.compile(valid_ip)
        vp2 = re.compile(valid_host)

        for arg in args:
            if (re.search(vp, arg)):
                continue
            elif (re.search(vp2, arg)):
                continue
        else:
            raise SystemExit("Invalid URl or IP")