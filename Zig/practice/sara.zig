const std = @import("std");
const CP = std.ChildProcess;
pub fn main() void {
    std.debug.print("Hola", .{});
    CP.exec("ls");
}
