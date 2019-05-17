import getpass
import json
import sys
from argparse import ArgumentParser

from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.wallet.wallet import KeyWallet

ZERO_ADDRESS = f"cx{'0'*40}"


def get_parser():
    arg_parser = ArgumentParser()
    subparsers = arg_parser.add_subparsers(title='Available commands', metavar='command',
                                           description='If you want to see help message of commands,'
                                                       'use "prep command -h"')
    subparsers.dest = 'command'
    subparsers.reqired = True

    parser_reg = subparsers.add_parser('register')
    parser_reg.add_argument('-j', '--json', required=True, help="")
    parser_reg.add_argument('-p', '--password', required=False)
    parser_reg.add_argument('-k', '--key', required=True)
    parser_reg.add_argument('-u', '--url', default="http://localhost:9000/api/v3")

    parser_unreg = subparsers.add_parser('unregister')
    parser_unreg.add_argument('-k', '--key', required=True)
    parser_unreg.add_argument('-p', '--password', required=False)
    parser_unreg.add_argument('-u', '--url', default="http://localhost:9000/api/v3")

    return arg_parser


def main():
    cmd_args = sys.argv[1:]
    parser = get_parser()

    args = parser.parse_args(cmd_args)
    command = args.command
    key_path = args.key
    password = args.password
    url = args.url
    icon_service = IconService(HTTPProvider(url))

    if password is None:
        password = getpass.getpass('Enter password : ')

    try:
        wallet = KeyWallet.load(key_path, password)
    except:
        print('invalid keystore file or invalid password')
        sys.exit(1)

    try:
        if command == 'register':
            json_path = args.json
            with open(json_path, mode='r') as prep_info:
                reg_info = json.load(prep_info)

            tx = CallTransactionBuilder().from_(wallet.get_address()).to(ZERO_ADDRESS).step_limit(100000000). \
                nid(3).nonce(100).method("registerPRepCandidate").params(reg_info).value(0).build()
            signed_data = SignedTransaction(tx, wallet)
            result = icon_service.send_transaction(signed_data)

        elif command == 'unregister':
            tx = CallTransactionBuilder().from_(wallet.get_address()).to(ZERO_ADDRESS). \
                step_limit(100000000).nid(3).nonce(100).method("unregisterPRepCandidate").value(0).build()
            signed_data = SignedTransaction(tx, wallet)
            result = icon_service.send_transaction(signed_data)
        else:
            print('unknown command')
            sys.exit(2)
        print("result: ", result)
        sys.exit(0)
    except BaseException as e:
        print(e)
        sys.exit(3)


if __name__ == '__main__':
    main()
