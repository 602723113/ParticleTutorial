double radius = // 圆的半径
Location location = // 你的坐标
for (int degree = 0; degree < 360; degree++) {
    double radians = Math.toRadians(degree);
    double x = radius * Math.cos(radians);
    double y = radius * Math.sin(radians);
    
    location.add(x, 0, z);
    location.getWorld().spawnParticle(Particle.FLAME, location, 0);
    location.subtract(x, 0, z);
}