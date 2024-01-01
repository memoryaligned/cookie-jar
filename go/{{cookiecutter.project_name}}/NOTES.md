# Standard Operating Procedure

NOTE: look to this video for more guidance

[https://www.youtube.com/watch?v=SSRIn5DAmyw](https://www.youtube.com/watch?v=SSRIn5DAmyw)

## A. Inversion of control for palettes of commands

Create the command pallet (net in this example):

```bash
mkdir cmd/net
cobra-cli add net
mv cmd/net.go cmd/net/net.go
```

file: cmd/net/net.go

1. change the package to net
2. make the netCmd public

file: cmd/root.go

```go
func addSubCommands() {
  rootCmd.AddCommand(net.NetCmd)
}
```
