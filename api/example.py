import requests

def get_skins(name):
    auth = "Ubi_v1 t=ewogICJ2ZXIiOiAiMSIsCiAgImFpZCI6ICJhZmI0YjQzYy1mMWY3LTQxYjctYmNlZi1hNjM1ZDhjODM4MjIiLAogICJlbnYiOiAiUHJvZCIsCiAgInNpZCI6ICI5MDI0YWMyNC00NGVlLTRhMWQtYTVkZi1iNjMzNTg1MDkzYWIiLAogICJ0eXAiOiAiSldFIiwKICAiZW5jIjogIkExMjhDQkMiLAogICJpdiI6ICJvb1R3SUlPMHNVX21ONDd4ZTBxVXBRIiwKICAiaW50IjogIkhTMjU2IiwKICAia2lkIjogImNmZDAxNDZlLTYwYzktNDJlMi1hNDY3LTQzNmVlNmZlNmI4YSIKfQ.xYDQCNbO-iorw_RCJS_ECvB5PYbKz6gRvNy1WWfZh7jLy853TIu_9UVpB_gfBR4YzhYcadrGJByKh82IHzVmwQsdZHtJ1lcjSLEoLjzGJq59m84WsI3VH7SMhE8-WJHOutU5ERFMA-5DUkdlY3PGQ_OrCm2csMyRvkF_LkuejXJA8TeXAdhDsP7-QOi7PriL06ZBR_PcuKZF0XOcN9BAaIL9iDyNwS5WnU_-7qRruLY-5OxCKD6N4bw92I6fhMH0PkOVFl-mqHTiVV9XFZ3z9jP2_r30fJca1K6xJ4lB_JTIQkmlPD8XiFsdJ5YZ-2BbMKnKXQkMmQXjo0EbvnoWCIF0ub3ko1fyT-EPSCPtGmJROUmnOUFl_C04IJvYiOvPhPN2daGllginufLGzEQlgwwwSO-4IxLTAZbiVKkYCcJ7kWt--8VMg3A_a-ZYhrQW3ve1aWQclLNnQQ0Ut6nY_e76JS4nflaKWsdFhMYPpks6ue16te14p2sLWhh0oEoeNo_S0sC6U0zA1bzzTZG018mKPYgNNB2-lv46qjwCf1gmrK3-XUxbzBtfsoqybiN33x-TDrJVB1OWV6t7ByL9vBEMSjQgKxoXGMpCZBgF1zJW34aJUuIJEOFbgCHUh7pu8_4lNaerD7oRSUdol9g--KJnvM3G7AgXWEZg2JWnkZQlT65HNfnNNjyrwZYfcKkkE6Ej8En0ttxDRF2i5XqEF36XCGdKk3Oj6eromd62pg7aUe7_vyhEQ0SOn-6smGINQhqDF_hHCqc5j49m7u2neGVhrW9UHt4egpxdStvWlJzSZ0nZ_XPRnvm4jbIYubjK1H0eRcxIgqpnLHQSKMtFS5i44KoqKFnlZybXbNlQxXfmxbB-5Z1k2KJ0tVc4soB6CmD65e9QAsF076iWqJM39aNRdOBMwS3Y5USn0rQIJt11TDOW4Gp3rQabXBXEXhuo27Gf_NjGXfcVcIFOqTVFiNxE-YbRjK_hbejWaaerSHICbJRx8tM666OG8kwaJFHsK3FRHJHZU6VmQzkYQHdpdpBDUpQWWZ8ljFg1Iv_dwdKYcAqUOvIkmPhuBYAk4Qt0MgUR2kNJjCa6lx6A7apv3g.X3W88iGIYbnCJ7O2qBCVUcSJkC4QElEIhpG4wHHWWYs"
    r = requests.get(f"http://127.0.0.1:8000/skins/{name}", headers={"auth": auth})
    return r.json()

if __name__ == "__main__":
    print(get_skins("godly"))
