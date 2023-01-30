from packages.service import UserContactConverter

get_token = "fFz8Z7OpPTSY7gpAFPrWntoMuo07ACjp"
post_token = "ZGF0YWNvc2U6MTk2RDExMTU0NTZENw=="
url = "https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app"

converter = UserContactConverter(
    url=url, method_get_token=get_token, method_post_token=post_token
)

for data in converter.get_users():
    try:
        transform_data = converter.prepare_payload(data)
        response = converter.create_contact(transform_data)
        print(response)

    except Exception as e:
        raise (e)

print("PROCESS FINISHED")
