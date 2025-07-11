# Configuration

The `config.toml` file is used to configure the lighting setup. It is a simple text file that is easy to edit.

## `[lights]` Section

The `[lights]` section is used to define the DMX addresses of your lighting fixtures.

*   `BARS`: An array of the starting DMX addresses for your Aputure Infinibars.
*   `STRIPS`: An array of the starting DMX addresses for your Epix Flex 20 LED strips.

Example:

```toml
[lights]
BARS = [1, 113, 225]
STRIPS = [350]
```

## `[colors]` Section

The `[colors]` section is used to define a set of preset colors that can be used in your lighting scripts. Each color is defined as an array of three integers, representing the red, green, and blue values (0-255).

Example:

```toml
[colors]
RED=[255,0,0]
GREEN=[0,255,0]
BLUE=[0,0,255]
```
