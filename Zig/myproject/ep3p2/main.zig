const std = @import("std");
var myVariable: u8 = 34;

pub fn main() void {
    myVariable += 1;
    std.debug.print("{d}", .{myVariable});
}
