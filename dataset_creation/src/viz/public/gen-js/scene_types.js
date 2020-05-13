//
// Autogenerated by Thrift Compiler (0.12.0)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//


BodyType = {
  'STATIC' : 1,
  'DYNAMIC' : 2
};
UserInputStatus = {
  'UNDEFINED' : 0,
  'NO_OCCLUSIONS' : 1,
  'HAD_OCCLUSIONS' : 2
};
Vector = function(args) {
  this.x = null;
  this.y = null;
  if (args) {
    if (args.x !== undefined && args.x !== null) {
      this.x = args.x;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field x is unset!');
    }
    if (args.y !== undefined && args.y !== null) {
      this.y = args.y;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field y is unset!');
    }
  }
};
Vector.prototype = {};
Vector.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.DOUBLE) {
        this.x = input.readDouble().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.DOUBLE) {
        this.y = input.readDouble().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Vector.prototype.write = function(output) {
  output.writeStructBegin('Vector');
  if (this.x !== null && this.x !== undefined) {
    output.writeFieldBegin('x', Thrift.Type.DOUBLE, 1);
    output.writeDouble(this.x);
    output.writeFieldEnd();
  }
  if (this.y !== null && this.y !== undefined) {
    output.writeFieldBegin('y', Thrift.Type.DOUBLE, 2);
    output.writeDouble(this.y);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

IntVector = function(args) {
  this.x = null;
  this.y = null;
  if (args) {
    if (args.x !== undefined && args.x !== null) {
      this.x = args.x;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field x is unset!');
    }
    if (args.y !== undefined && args.y !== null) {
      this.y = args.y;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field y is unset!');
    }
  }
};
IntVector.prototype = {};
IntVector.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.I32) {
        this.x = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I32) {
        this.y = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

IntVector.prototype.write = function(output) {
  output.writeStructBegin('IntVector');
  if (this.x !== null && this.x !== undefined) {
    output.writeFieldBegin('x', Thrift.Type.I32, 1);
    output.writeI32(this.x);
    output.writeFieldEnd();
  }
  if (this.y !== null && this.y !== undefined) {
    output.writeFieldBegin('y', Thrift.Type.I32, 2);
    output.writeI32(this.y);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Polygon = function(args) {
  this.vertices = null;
  if (args) {
    if (args.vertices !== undefined && args.vertices !== null) {
      this.vertices = Thrift.copyList(args.vertices, [Vector]);
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field vertices is unset!');
    }
  }
};
Polygon.prototype = {};
Polygon.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.vertices = [];
        var _rtmp31 = input.readListBegin();
        var _size0 = _rtmp31.size || 0;
        for (var _i2 = 0; _i2 < _size0; ++_i2) {
          var elem3 = null;
          elem3 = new Vector();
          elem3.read(input);
          this.vertices.push(elem3);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Polygon.prototype.write = function(output) {
  output.writeStructBegin('Polygon');
  if (this.vertices !== null && this.vertices !== undefined) {
    output.writeFieldBegin('vertices', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.STRUCT, this.vertices.length);
    for (var iter4 in this.vertices) {
      if (this.vertices.hasOwnProperty(iter4)) {
        iter4 = this.vertices[iter4];
        iter4.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Circle = function(args) {
  this.radius = null;
  if (args) {
    if (args.radius !== undefined && args.radius !== null) {
      this.radius = args.radius;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field radius is unset!');
    }
  }
};
Circle.prototype = {};
Circle.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.DOUBLE) {
        this.radius = input.readDouble().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Circle.prototype.write = function(output) {
  output.writeStructBegin('Circle');
  if (this.radius !== null && this.radius !== undefined) {
    output.writeFieldBegin('radius', Thrift.Type.DOUBLE, 1);
    output.writeDouble(this.radius);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Shape = function(args) {
  this.polygon = null;
  this.circle = null;
  if (args) {
    if (args.polygon !== undefined && args.polygon !== null) {
      this.polygon = new Polygon(args.polygon);
    }
    if (args.circle !== undefined && args.circle !== null) {
      this.circle = new Circle(args.circle);
    }
  }
};
Shape.prototype = {};
Shape.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.polygon = new Polygon();
        this.polygon.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.circle = new Circle();
        this.circle.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Shape.prototype.write = function(output) {
  output.writeStructBegin('Shape');
  if (this.polygon !== null && this.polygon !== undefined) {
    output.writeFieldBegin('polygon', Thrift.Type.STRUCT, 1);
    this.polygon.write(output);
    output.writeFieldEnd();
  }
  if (this.circle !== null && this.circle !== undefined) {
    output.writeFieldBegin('circle', Thrift.Type.STRUCT, 2);
    this.circle.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Body = function(args) {
  this.position = null;
  this.bodyType = null;
  this.angle = 0.0000000000000000;
  this.shapes = null;
  this.color = null;
  if (args) {
    if (args.position !== undefined && args.position !== null) {
      this.position = new Vector(args.position);
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field position is unset!');
    }
    if (args.bodyType !== undefined && args.bodyType !== null) {
      this.bodyType = args.bodyType;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field bodyType is unset!');
    }
    if (args.angle !== undefined && args.angle !== null) {
      this.angle = args.angle;
    }
    if (args.shapes !== undefined && args.shapes !== null) {
      this.shapes = Thrift.copyList(args.shapes, [Shape]);
    }
    if (args.color !== undefined && args.color !== null) {
      this.color = args.color;
    }
  }
};
Body.prototype = {};
Body.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.position = new Vector();
        this.position.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I32) {
        this.bodyType = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.DOUBLE) {
        this.angle = input.readDouble().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 4:
      if (ftype == Thrift.Type.LIST) {
        this.shapes = [];
        var _rtmp36 = input.readListBegin();
        var _size5 = _rtmp36.size || 0;
        for (var _i7 = 0; _i7 < _size5; ++_i7) {
          var elem8 = null;
          elem8 = new Shape();
          elem8.read(input);
          this.shapes.push(elem8);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 5:
      if (ftype == Thrift.Type.I32) {
        this.color = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Body.prototype.write = function(output) {
  output.writeStructBegin('Body');
  if (this.position !== null && this.position !== undefined) {
    output.writeFieldBegin('position', Thrift.Type.STRUCT, 1);
    this.position.write(output);
    output.writeFieldEnd();
  }
  if (this.bodyType !== null && this.bodyType !== undefined) {
    output.writeFieldBegin('bodyType', Thrift.Type.I32, 2);
    output.writeI32(this.bodyType);
    output.writeFieldEnd();
  }
  if (this.angle !== null && this.angle !== undefined) {
    output.writeFieldBegin('angle', Thrift.Type.DOUBLE, 3);
    output.writeDouble(this.angle);
    output.writeFieldEnd();
  }
  if (this.shapes !== null && this.shapes !== undefined) {
    output.writeFieldBegin('shapes', Thrift.Type.LIST, 4);
    output.writeListBegin(Thrift.Type.STRUCT, this.shapes.length);
    for (var iter9 in this.shapes) {
      if (this.shapes.hasOwnProperty(iter9)) {
        iter9 = this.shapes[iter9];
        iter9.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.color !== null && this.color !== undefined) {
    output.writeFieldBegin('color', Thrift.Type.I32, 5);
    output.writeI32(this.color);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

AbsoluteConvexPolygon = function(args) {
  this.vertices = null;
  if (args) {
    if (args.vertices !== undefined && args.vertices !== null) {
      this.vertices = Thrift.copyList(args.vertices, [Vector]);
    }
  }
};
AbsoluteConvexPolygon.prototype = {};
AbsoluteConvexPolygon.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.vertices = [];
        var _rtmp311 = input.readListBegin();
        var _size10 = _rtmp311.size || 0;
        for (var _i12 = 0; _i12 < _size10; ++_i12) {
          var elem13 = null;
          elem13 = new Vector();
          elem13.read(input);
          this.vertices.push(elem13);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AbsoluteConvexPolygon.prototype.write = function(output) {
  output.writeStructBegin('AbsoluteConvexPolygon');
  if (this.vertices !== null && this.vertices !== undefined) {
    output.writeFieldBegin('vertices', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.STRUCT, this.vertices.length);
    for (var iter14 in this.vertices) {
      if (this.vertices.hasOwnProperty(iter14)) {
        iter14 = this.vertices[iter14];
        iter14.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

CircleWithPosition = function(args) {
  this.position = null;
  this.radius = null;
  if (args) {
    if (args.position !== undefined && args.position !== null) {
      this.position = new Vector(args.position);
    }
    if (args.radius !== undefined && args.radius !== null) {
      this.radius = args.radius;
    }
  }
};
CircleWithPosition.prototype = {};
CircleWithPosition.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.position = new Vector();
        this.position.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.DOUBLE) {
        this.radius = input.readDouble().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

CircleWithPosition.prototype.write = function(output) {
  output.writeStructBegin('CircleWithPosition');
  if (this.position !== null && this.position !== undefined) {
    output.writeFieldBegin('position', Thrift.Type.STRUCT, 1);
    this.position.write(output);
    output.writeFieldEnd();
  }
  if (this.radius !== null && this.radius !== undefined) {
    output.writeFieldBegin('radius', Thrift.Type.DOUBLE, 2);
    output.writeDouble(this.radius);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

UserInput = function(args) {
  this.polygons = null;
  this.balls = null;
  this.flattened_point_list = null;
  if (args) {
    if (args.polygons !== undefined && args.polygons !== null) {
      this.polygons = Thrift.copyList(args.polygons, [AbsoluteConvexPolygon]);
    }
    if (args.balls !== undefined && args.balls !== null) {
      this.balls = Thrift.copyList(args.balls, [CircleWithPosition]);
    }
    if (args.flattened_point_list !== undefined && args.flattened_point_list !== null) {
      this.flattened_point_list = Thrift.copyList(args.flattened_point_list, [null]);
    }
  }
};
UserInput.prototype = {};
UserInput.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.polygons = [];
        var _rtmp316 = input.readListBegin();
        var _size15 = _rtmp316.size || 0;
        for (var _i17 = 0; _i17 < _size15; ++_i17) {
          var elem18 = null;
          elem18 = new AbsoluteConvexPolygon();
          elem18.read(input);
          this.polygons.push(elem18);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.LIST) {
        this.balls = [];
        var _rtmp320 = input.readListBegin();
        var _size19 = _rtmp320.size || 0;
        for (var _i21 = 0; _i21 < _size19; ++_i21) {
          var elem22 = null;
          elem22 = new CircleWithPosition();
          elem22.read(input);
          this.balls.push(elem22);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.LIST) {
        this.flattened_point_list = [];
        var _rtmp324 = input.readListBegin();
        var _size23 = _rtmp324.size || 0;
        for (var _i25 = 0; _i25 < _size23; ++_i25) {
          var elem26 = null;
          elem26 = input.readI32().value;
          this.flattened_point_list.push(elem26);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

UserInput.prototype.write = function(output) {
  output.writeStructBegin('UserInput');
  if (this.polygons !== null && this.polygons !== undefined) {
    output.writeFieldBegin('polygons', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.STRUCT, this.polygons.length);
    for (var iter27 in this.polygons) {
      if (this.polygons.hasOwnProperty(iter27)) {
        iter27 = this.polygons[iter27];
        iter27.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.balls !== null && this.balls !== undefined) {
    output.writeFieldBegin('balls', Thrift.Type.LIST, 2);
    output.writeListBegin(Thrift.Type.STRUCT, this.balls.length);
    for (var iter28 in this.balls) {
      if (this.balls.hasOwnProperty(iter28)) {
        iter28 = this.balls[iter28];
        iter28.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.flattened_point_list !== null && this.flattened_point_list !== undefined) {
    output.writeFieldBegin('flattened_point_list', Thrift.Type.LIST, 3);
    output.writeListBegin(Thrift.Type.I32, this.flattened_point_list.length);
    for (var iter29 in this.flattened_point_list) {
      if (this.flattened_point_list.hasOwnProperty(iter29)) {
        iter29 = this.flattened_point_list[iter29];
        output.writeI32(iter29);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Scene = function(args) {
  this.bodies = null;
  this.user_input_bodies = null;
  this.width = null;
  this.height = null;
  this.user_input_status = 0;
  if (args) {
    if (args.bodies !== undefined && args.bodies !== null) {
      this.bodies = Thrift.copyList(args.bodies, [Body]);
    }
    if (args.user_input_bodies !== undefined && args.user_input_bodies !== null) {
      this.user_input_bodies = Thrift.copyList(args.user_input_bodies, [Body]);
    }
    if (args.width !== undefined && args.width !== null) {
      this.width = args.width;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field width is unset!');
    }
    if (args.height !== undefined && args.height !== null) {
      this.height = args.height;
    } else {
      throw new Thrift.TProtocolException(Thrift.TProtocolExceptionType.UNKNOWN, 'Required field height is unset!');
    }
    if (args.user_input_status !== undefined && args.user_input_status !== null) {
      this.user_input_status = args.user_input_status;
    }
  }
};
Scene.prototype = {};
Scene.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.bodies = [];
        var _rtmp331 = input.readListBegin();
        var _size30 = _rtmp331.size || 0;
        for (var _i32 = 0; _i32 < _size30; ++_i32) {
          var elem33 = null;
          elem33 = new Body();
          elem33.read(input);
          this.bodies.push(elem33);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.LIST) {
        this.user_input_bodies = [];
        var _rtmp335 = input.readListBegin();
        var _size34 = _rtmp335.size || 0;
        for (var _i36 = 0; _i36 < _size34; ++_i36) {
          var elem37 = null;
          elem37 = new Body();
          elem37.read(input);
          this.user_input_bodies.push(elem37);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.I32) {
        this.width = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 4:
      if (ftype == Thrift.Type.I32) {
        this.height = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 5:
      if (ftype == Thrift.Type.I32) {
        this.user_input_status = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Scene.prototype.write = function(output) {
  output.writeStructBegin('Scene');
  if (this.bodies !== null && this.bodies !== undefined) {
    output.writeFieldBegin('bodies', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.STRUCT, this.bodies.length);
    for (var iter38 in this.bodies) {
      if (this.bodies.hasOwnProperty(iter38)) {
        iter38 = this.bodies[iter38];
        iter38.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.user_input_bodies !== null && this.user_input_bodies !== undefined) {
    output.writeFieldBegin('user_input_bodies', Thrift.Type.LIST, 2);
    output.writeListBegin(Thrift.Type.STRUCT, this.user_input_bodies.length);
    for (var iter39 in this.user_input_bodies) {
      if (this.user_input_bodies.hasOwnProperty(iter39)) {
        iter39 = this.user_input_bodies[iter39];
        iter39.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.width !== null && this.width !== undefined) {
    output.writeFieldBegin('width', Thrift.Type.I32, 3);
    output.writeI32(this.width);
    output.writeFieldEnd();
  }
  if (this.height !== null && this.height !== undefined) {
    output.writeFieldBegin('height', Thrift.Type.I32, 4);
    output.writeI32(this.height);
    output.writeFieldEnd();
  }
  if (this.user_input_status !== null && this.user_input_status !== undefined) {
    output.writeFieldBegin('user_input_status', Thrift.Type.I32, 5);
    output.writeI32(this.user_input_status);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Solution = function(args) {
  this.points = null;
  if (args) {
    if (args.points !== undefined && args.points !== null) {
      this.points = Thrift.copyList(args.points, [IntVector]);
    }
  }
};
Solution.prototype = {};
Solution.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.points = [];
        var _rtmp341 = input.readListBegin();
        var _size40 = _rtmp341.size || 0;
        for (var _i42 = 0; _i42 < _size40; ++_i42) {
          var elem43 = null;
          elem43 = new IntVector();
          elem43.read(input);
          this.points.push(elem43);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Solution.prototype.write = function(output) {
  output.writeStructBegin('Solution');
  if (this.points !== null && this.points !== undefined) {
    output.writeFieldBegin('points', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.STRUCT, this.points.length);
    for (var iter44 in this.points) {
      if (this.points.hasOwnProperty(iter44)) {
        iter44 = this.points[iter44];
        iter44.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Image = function(args) {
  this.values = null;
  this.height = null;
  this.width = null;
  if (args) {
    if (args.values !== undefined && args.values !== null) {
      this.values = Thrift.copyList(args.values, [null]);
    }
    if (args.height !== undefined && args.height !== null) {
      this.height = args.height;
    }
    if (args.width !== undefined && args.width !== null) {
      this.width = args.width;
    }
  }
};
Image.prototype = {};
Image.prototype.read = function(input) {
  input.readStructBegin();
  while (true) {
    var ret = input.readFieldBegin();
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid) {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        this.values = [];
        var _rtmp346 = input.readListBegin();
        var _size45 = _rtmp346.size || 0;
        for (var _i47 = 0; _i47 < _size45; ++_i47) {
          var elem48 = null;
          elem48 = input.readI32().value;
          this.values.push(elem48);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I32) {
        this.height = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.I32) {
        this.width = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Image.prototype.write = function(output) {
  output.writeStructBegin('Image');
  if (this.values !== null && this.values !== undefined) {
    output.writeFieldBegin('values', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.I32, this.values.length);
    for (var iter49 in this.values) {
      if (this.values.hasOwnProperty(iter49)) {
        iter49 = this.values[iter49];
        output.writeI32(iter49);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.height !== null && this.height !== undefined) {
    output.writeFieldBegin('height', Thrift.Type.I32, 2);
    output.writeI32(this.height);
    output.writeFieldEnd();
  }
  if (this.width !== null && this.width !== undefined) {
    output.writeFieldBegin('width', Thrift.Type.I32, 3);
    output.writeI32(this.width);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

