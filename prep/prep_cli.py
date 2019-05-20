import getpass
import json
import sys
from argparse import ArgumentParser

from iconsdk.builder.call_builder import CallBuilder
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

    parser_candidate = subparsers.add_parser('candidate')
    parser_candidate.add_argument('-u', '--url', default="http://localhost:9000/api/v3")
    parser_candidate.add_argument('-j', '--json', required=False)

    return arg_parser


def get_wallet(args: dict) -> KeyWallet:
    key_path = args.get('key')
    password = args.get('password')
    if password is None:
        getpass.getpass('Enter password : ')
    try:
        wallet = KeyWallet.load(key_path, password)
        return wallet
    except:
        print('invalid keystore file or wrong password')
        sys.exit(1)


def main():
    cmd_args = sys.argv[1:]
    parser = get_parser()

    args = vars(parser.parse_args(cmd_args))
    command = args.get('command')
    url = args.get('url')
    icon_service = IconService(HTTPProvider(url))

    try:
        if command == 'register':
            wallet = get_wallet(args)
            json_path = args.get('json')
            with open(json_path, mode='r') as prep_info:
                reg_info = json.load(prep_info)
            public_key = wallet.bytes_public_key
            reg_info['publicKey'] = f"0x{public_key.hex()}"

            tx = CallTransactionBuilder().from_(wallet.get_address()).to(ZERO_ADDRESS).step_limit(100000000). \
                nid(3).nonce(100).method("registerPRepCandidate").params(reg_info).value(0).build()
            signed_data = SignedTransaction(tx, wallet)
            result = icon_service.send_transaction(signed_data)
        elif command == 'unregister':
            wallet = get_wallet(args)
            tx = CallTransactionBuilder().from_(wallet.get_address()).to(ZERO_ADDRESS). \
                step_limit(100000000).nid(3).nonce(100).method("unregisterPRepCandidate").value(0).build()
            signed_data = SignedTransaction(tx, wallet)
            result = icon_service.send_transaction(signed_data)
        elif command == 'candidate':
            json_path = args.get('json')
            if json_path is not None:
                with open(json_path, mode='r') as prep_info:
                    params = json.load(prep_info)
            else:
                params = {}
            call_data = CallBuilder(from_=f"hx{'0'*40}", to=ZERO_ADDRESS,
                                    method="getPRepCandidateList").params(params).build()
            result = icon_service.call(call_data)
        else:
            print('unknown command')
            sys.exit(2)
        print('result : ', result)
        return 0
    except BaseException as e:
        print(e)
        sys.exit(3)


if __name__ == '__main__':
    main()
