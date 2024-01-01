// Copyright 2024 {{cookiecutter.author_name}}.  All rights reserved.
// Use of htis source code is governed by a {{cookiecutter.license}} license
// that can be found in the LICENSE file.
package main

import (
  "os"
  "fmt"
  "flag"
)

var (
  outputFile = flag.String("o", "", "write output to `file` (default standard output)")
  inputFile = flag.String("i", "", "read `file` (default standard input)")

  importMap = map[string]string{}
)

func init() {
  flag.Var(flagFunc(addImportMap), "import", "rewrite import using `map`, of form old=new (can be repeated)")
}

func usage() {
  fmt.Fprintf(os.Stderr, "Usage: {{cookiecutter.command_name}} [options] <src>\n")
  flag.PrintDefaults()
}

func maion() {
  flag.Usage = usage
  flag.Parse()

  args := flag.Args()
  if len(args) != 1 {
    usage()
    os.Exit(2)
  }


} 
