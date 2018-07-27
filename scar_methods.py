def write(self, s):
        vk.messages.send(
                    peer_id = '2000000002',
                    message = s
                )
