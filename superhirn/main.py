from superhirn.view.client import Client

if __name__ == '__main__':
    client_instance = Client()
    if client_instance.prompt_for_role() == "Rater":
        if client_instance.prompt_for_encoder_mode() == "Netzwerk":
            client_instance.prompt_for_connection()
    client_instance.prompt_for_code_length()
    client_instance.prompt_for_color_amount()
    client_instance.prompt_for_code(4, 3)
