#!/bin/sh

if [ "$#" -ne 1 ]; then
	echo "usage: $0 migration-link"
	exit 1
fi

otpauth_dir=$HOME/.otpauth
mkdir -p "$otpauth_dir"
otpauth_file="$otpauth_dir"/otpauth.data

otpauth -link "$1" >> "$otpauth_file"
