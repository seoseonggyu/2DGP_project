//////////////////////////////////////////
//
// NOTE: This is *not* a valid shader file
//
///////////////////////////////////////////
Shader "Brave/Internal/DistortionWave" {
Properties {
_MainTex ("Base (RGB)", 2D) = "white" { }
_WaveCenter ("Wave Center", Vector) = (0,0,0,0)
_DistortProgress ("Distort Progress", Range(0, 1)) = 0
}
SubShader {
 Pass {
  GpuProgramID 35351
Program "vp" {
SubProgram "d3d11 " {
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
"#ifdef VERTEX
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 hlslcc_mtx4x4unity_ObjectToWorld[4];
uniform 	vec4 hlslcc_mtx4x4unity_MatrixVP[4];
in  vec4 in_POSITION0;
in  vec2 in_TEXCOORD0;
out vec2 vs_TEXCOORD0;
vec4 u_xlat0;
vec4 u_xlat1;
void main()
{
    u_xlat0 = in_POSITION0.yyyy * hlslcc_mtx4x4unity_ObjectToWorld[1];
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[0] * in_POSITION0.xxxx + u_xlat0;
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[2] * in_POSITION0.zzzz + u_xlat0;
    u_xlat0 = u_xlat0 + hlslcc_mtx4x4unity_ObjectToWorld[3];
    u_xlat1 = u_xlat0.yyyy * hlslcc_mtx4x4unity_MatrixVP[1];
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[0] * u_xlat0.xxxx + u_xlat1;
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[2] * u_xlat0.zzzz + u_xlat1;
    gl_Position = hlslcc_mtx4x4unity_MatrixVP[3] * u_xlat0.wwww + u_xlat1;
    vs_TEXCOORD0.xy = in_TEXCOORD0.xy;
    return;
}

#endif
#ifdef FRAGMENT
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 _WaveCenter;
uniform 	float _DistortProgress;
uniform  sampler2D _MainTex;
in  vec2 vs_TEXCOORD0;
layout(location = 0) out vec4 SV_Target0;
vec4 u_xlat0;
float u_xlat2;
float u_xlat3;
void main()
{
    u_xlat0.xy = vs_TEXCOORD0.xy + (-_WaveCenter.xy);
    u_xlat0.zw = u_xlat0.xx * vec2(1.77777779, 1.77777779);
    u_xlat2 = dot(u_xlat0.yz, u_xlat0.yw);
    u_xlat0.xy = u_xlat0.xy * vec2(1.77777779, 1.0);
    u_xlat0.xy = u_xlat0.xy * _WaveCenter.ww;
    u_xlat2 = sqrt(u_xlat2);
    u_xlat2 = _DistortProgress * 2.0 + (-u_xlat2);
    u_xlat2 = abs(u_xlat2) / _WaveCenter.z;
    u_xlat2 = clamp(u_xlat2, 0.0, 1.0);
    u_xlat2 = (-u_xlat2) + 1.0;
    u_xlat3 = u_xlat2 * u_xlat2;
    u_xlat2 = u_xlat3 * u_xlat2;
    u_xlat0.xy = u_xlat0.xy * vec2(u_xlat2) + vs_TEXCOORD0.xy;
    SV_Target0 = texture(_MainTex, u_xlat0.xy);
    return;
}

#endif
"
}
SubProgram "vulkan " {
"; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 94
; Schema: 0
                                              OpCapability Shader 
                                       %1 = OpExtInstImport "GLSL.std.450" 
                                              OpMemoryModel Logical GLSL450 
                                              OpEntryPoint Vertex %4 "main" %11 %72 %84 %86 
                                              OpDecorate %11 Location 11 
                                              OpDecorate %16 ArrayStride 16 
                                              OpDecorate %17 ArrayStride 17 
                                              OpMemberDecorate %18 0 Offset 18 
                                              OpMemberDecorate %18 1 Offset 18 
                                              OpDecorate %18 Block 
                                              OpDecorate %20 DescriptorSet 20 
                                              OpDecorate %20 Binding 20 
                                              OpMemberDecorate %70 0 BuiltIn 70 
                                              OpMemberDecorate %70 1 BuiltIn 70 
                                              OpMemberDecorate %70 2 BuiltIn 70 
                                              OpDecorate %70 Block 
                                              OpDecorate %84 RelaxedPrecision 
                                              OpDecorate %84 Location 84 
                                              OpDecorate %86 RelaxedPrecision 
                                              OpDecorate %86 Location 86 
                                              OpDecorate %87 RelaxedPrecision 
                                       %2 = OpTypeVoid 
                                       %3 = OpTypeFunction %2 
                                       %6 = OpTypeFloat 32 
                                       %7 = OpTypeVector %6 4 
                                       %8 = OpTypePointer Private %7 
                        Private f32_4* %9 = OpVariable Private 
                                      %10 = OpTypePointer Input %7 
                         Input f32_4* %11 = OpVariable Input 
                                      %14 = OpTypeInt 32 0 
                                  u32 %15 = OpConstant 4 
                                      %16 = OpTypeArray %7 %15 
                                      %17 = OpTypeArray %7 %15 
                                      %18 = OpTypeStruct %16 %17 
                                      %19 = OpTypePointer Uniform %18 
Uniform struct {f32_4[4]; f32_4[4];}* %20 = OpVariable Uniform 
                                      %21 = OpTypeInt 32 1 
                                  i32 %22 = OpConstant 0 
                                  i32 %23 = OpConstant 1 
                                      %24 = OpTypePointer Uniform %7 
                                  i32 %35 = OpConstant 2 
                                  i32 %44 = OpConstant 3 
                       Private f32_4* %48 = OpVariable Private 
                                  u32 %68 = OpConstant 1 
                                      %69 = OpTypeArray %6 %68 
                                      %70 = OpTypeStruct %7 %6 %69 
                                      %71 = OpTypePointer Output %70 
 Output struct {f32_4; f32; f32[1];}* %72 = OpVariable Output 
                                      %80 = OpTypePointer Output %7 
                                      %82 = OpTypeVector %6 2 
                                      %83 = OpTypePointer Output %82 
                        Output f32_2* %84 = OpVariable Output 
                                      %85 = OpTypePointer Input %82 
                         Input f32_2* %86 = OpVariable Input 
                                      %88 = OpTypePointer Output %6 
                                  void %4 = OpFunction None %3 
                                       %5 = OpLabel 
                                f32_4 %12 = OpLoad %11 
                                f32_4 %13 = OpVectorShuffle %12 %12 1 1 1 1 
                       Uniform f32_4* %25 = OpAccessChain %20 %22 %23 
                                f32_4 %26 = OpLoad %25 
                                f32_4 %27 = OpFMul %13 %26 
                                              OpStore %9 %27 
                       Uniform f32_4* %28 = OpAccessChain %20 %22 %22 
                                f32_4 %29 = OpLoad %28 
                                f32_4 %30 = OpLoad %11 
                                f32_4 %31 = OpVectorShuffle %30 %30 0 0 0 0 
                                f32_4 %32 = OpFMul %29 %31 
                                f32_4 %33 = OpLoad %9 
                                f32_4 %34 = OpFAdd %32 %33 
                                              OpStore %9 %34 
                       Uniform f32_4* %36 = OpAccessChain %20 %22 %35 
                                f32_4 %37 = OpLoad %36 
                                f32_4 %38 = OpLoad %11 
                                f32_4 %39 = OpVectorShuffle %38 %38 2 2 2 2 
                                f32_4 %40 = OpFMul %37 %39 
                                f32_4 %41 = OpLoad %9 
                                f32_4 %42 = OpFAdd %40 %41 
                                              OpStore %9 %42 
                                f32_4 %43 = OpLoad %9 
                       Uniform f32_4* %45 = OpAccessChain %20 %22 %44 
                                f32_4 %46 = OpLoad %45 
                                f32_4 %47 = OpFAdd %43 %46 
                                              OpStore %9 %47 
                                f32_4 %49 = OpLoad %9 
                                f32_4 %50 = OpVectorShuffle %49 %49 1 1 1 1 
                       Uniform f32_4* %51 = OpAccessChain %20 %23 %23 
                                f32_4 %52 = OpLoad %51 
                                f32_4 %53 = OpFMul %50 %52 
                                              OpStore %48 %53 
                       Uniform f32_4* %54 = OpAccessChain %20 %23 %22 
                                f32_4 %55 = OpLoad %54 
                                f32_4 %56 = OpLoad %9 
                                f32_4 %57 = OpVectorShuffle %56 %56 0 0 0 0 
                                f32_4 %58 = OpFMul %55 %57 
                                f32_4 %59 = OpLoad %48 
                                f32_4 %60 = OpFAdd %58 %59 
                                              OpStore %48 %60 
                       Uniform f32_4* %61 = OpAccessChain %20 %23 %35 
                                f32_4 %62 = OpLoad %61 
                                f32_4 %63 = OpLoad %9 
                                f32_4 %64 = OpVectorShuffle %63 %63 2 2 2 2 
                                f32_4 %65 = OpFMul %62 %64 
                                f32_4 %66 = OpLoad %48 
                                f32_4 %67 = OpFAdd %65 %66 
                                              OpStore %48 %67 
                       Uniform f32_4* %73 = OpAccessChain %20 %23 %44 
                                f32_4 %74 = OpLoad %73 
                                f32_4 %75 = OpLoad %9 
                                f32_4 %76 = OpVectorShuffle %75 %75 3 3 3 3 
                                f32_4 %77 = OpFMul %74 %76 
                                f32_4 %78 = OpLoad %48 
                                f32_4 %79 = OpFAdd %77 %78 
                        Output f32_4* %81 = OpAccessChain %72 %22 
                                              OpStore %81 %79 
                                f32_2 %87 = OpLoad %86 
                                              OpStore %84 %87 
                          Output f32* %89 = OpAccessChain %72 %22 %68 
                                  f32 %90 = OpLoad %89 
                                  f32 %91 = OpFNegate %90 
                          Output f32* %92 = OpAccessChain %72 %22 %68 
                                              OpStore %92 %91 
                                              OpReturn
                                              OpFunctionEnd
; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 107
; Schema: 0
                                                     OpCapability Shader 
                                              %1 = OpExtInstImport "GLSL.std.450" 
                                                     OpMemoryModel Logical GLSL450 
                                                     OpEntryPoint Fragment %4 "main" %12 %97 
                                                     OpExecutionMode %4 OriginUpperLeft 
                                                     OpDecorate %12 RelaxedPrecision 
                                                     OpDecorate %12 Location 12 
                                                     OpDecorate %13 RelaxedPrecision 
                                                     OpMemberDecorate %14 0 Offset 14 
                                                     OpMemberDecorate %14 1 Offset 14 
                                                     OpDecorate %14 Block 
                                                     OpDecorate %16 DescriptorSet 16 
                                                     OpDecorate %16 Binding 16 
                                                     OpDecorate %92 RelaxedPrecision 
                                                     OpDecorate %97 Location 97 
                                                     OpDecorate %101 RelaxedPrecision 
                                                     OpDecorate %101 DescriptorSet 101 
                                                     OpDecorate %101 Binding 101 
                                                     OpDecorate %102 RelaxedPrecision 
                                              %2 = OpTypeVoid 
                                              %3 = OpTypeFunction %2 
                                              %6 = OpTypeFloat 32 
                                              %7 = OpTypeVector %6 4 
                                              %8 = OpTypePointer Private %7 
                               Private f32_4* %9 = OpVariable Private 
                                             %10 = OpTypeVector %6 2 
                                             %11 = OpTypePointer Input %10 
                                Input f32_2* %12 = OpVariable Input 
                                             %14 = OpTypeStruct %7 %6 
                                             %15 = OpTypePointer Uniform %14 
               Uniform struct {f32_4; f32;}* %16 = OpVariable Uniform 
                                             %17 = OpTypeInt 32 1 
                                         i32 %18 = OpConstant 0 
                                             %19 = OpTypePointer Uniform %7 
                                         f32 %29 = OpConstant 3.674022E-40 
                                       f32_2 %30 = OpConstantComposite %29 %29 
                                             %34 = OpTypePointer Private %6 
                                Private f32* %35 = OpVariable Private 
                                         f32 %43 = OpConstant 3.674022E-40 
                                       f32_2 %44 = OpConstantComposite %29 %43 
                                         i32 %58 = OpConstant 1 
                                             %59 = OpTypePointer Uniform %6 
                                         f32 %62 = OpConstant 3.674022E-40 
                                             %69 = OpTypeInt 32 0 
                                         u32 %70 = OpConstant 2 
                                         f32 %75 = OpConstant 3.674022E-40 
                                Private f32* %80 = OpVariable Private 
                                             %96 = OpTypePointer Output %7 
                               Output f32_4* %97 = OpVariable Output 
                                             %98 = OpTypeImage %6 Dim2D 0 0 0 1 Unknown 
                                             %99 = OpTypeSampledImage %98 
                                            %100 = OpTypePointer UniformConstant %99 
UniformConstant read_only Texture2DSampled* %101 = OpVariable UniformConstant 
                                         void %4 = OpFunction None %3 
                                              %5 = OpLabel 
                                       f32_2 %13 = OpLoad %12 
                              Uniform f32_4* %20 = OpAccessChain %16 %18 
                                       f32_4 %21 = OpLoad %20 
                                       f32_2 %22 = OpVectorShuffle %21 %21 0 1 
                                       f32_2 %23 = OpFNegate %22 
                                       f32_2 %24 = OpFAdd %13 %23 
                                       f32_4 %25 = OpLoad %9 
                                       f32_4 %26 = OpVectorShuffle %25 %24 4 5 2 3 
                                                     OpStore %9 %26 
                                       f32_4 %27 = OpLoad %9 
                                       f32_2 %28 = OpVectorShuffle %27 %27 0 0 
                                       f32_2 %31 = OpFMul %28 %30 
                                       f32_4 %32 = OpLoad %9 
                                       f32_4 %33 = OpVectorShuffle %32 %31 0 1 4 5 
                                                     OpStore %9 %33 
                                       f32_4 %36 = OpLoad %9 
                                       f32_2 %37 = OpVectorShuffle %36 %36 1 2 
                                       f32_4 %38 = OpLoad %9 
                                       f32_2 %39 = OpVectorShuffle %38 %38 1 3 
                                         f32 %40 = OpDot %37 %39 
                                                     OpStore %35 %40 
                                       f32_4 %41 = OpLoad %9 
                                       f32_2 %42 = OpVectorShuffle %41 %41 0 1 
                                       f32_2 %45 = OpFMul %42 %44 
                                       f32_4 %46 = OpLoad %9 
                                       f32_4 %47 = OpVectorShuffle %46 %45 4 5 2 3 
                                                     OpStore %9 %47 
                                       f32_4 %48 = OpLoad %9 
                                       f32_2 %49 = OpVectorShuffle %48 %48 0 1 
                              Uniform f32_4* %50 = OpAccessChain %16 %18 
                                       f32_4 %51 = OpLoad %50 
                                       f32_2 %52 = OpVectorShuffle %51 %51 3 3 
                                       f32_2 %53 = OpFMul %49 %52 
                                       f32_4 %54 = OpLoad %9 
                                       f32_4 %55 = OpVectorShuffle %54 %53 4 5 2 3 
                                                     OpStore %9 %55 
                                         f32 %56 = OpLoad %35 
                                         f32 %57 = OpExtInst %1 31 %56 
                                                     OpStore %35 %57 
                                Uniform f32* %60 = OpAccessChain %16 %58 
                                         f32 %61 = OpLoad %60 
                                         f32 %63 = OpFMul %61 %62 
                                         f32 %64 = OpLoad %35 
                                         f32 %65 = OpFNegate %64 
                                         f32 %66 = OpFAdd %63 %65 
                                                     OpStore %35 %66 
                                         f32 %67 = OpLoad %35 
                                         f32 %68 = OpExtInst %1 4 %67 
                                Uniform f32* %71 = OpAccessChain %16 %18 %70 
                                         f32 %72 = OpLoad %71 
                                         f32 %73 = OpFDiv %68 %72 
                                                     OpStore %35 %73 
                                         f32 %74 = OpLoad %35 
                                         f32 %76 = OpExtInst %1 43 %74 %75 %43 
                                                     OpStore %35 %76 
                                         f32 %77 = OpLoad %35 
                                         f32 %78 = OpFNegate %77 
                                         f32 %79 = OpFAdd %78 %43 
                                                     OpStore %35 %79 
                                         f32 %81 = OpLoad %35 
                                         f32 %82 = OpLoad %35 
                                         f32 %83 = OpFMul %81 %82 
                                                     OpStore %80 %83 
                                         f32 %84 = OpLoad %80 
                                         f32 %85 = OpLoad %35 
                                         f32 %86 = OpFMul %84 %85 
                                                     OpStore %35 %86 
                                       f32_4 %87 = OpLoad %9 
                                       f32_2 %88 = OpVectorShuffle %87 %87 0 1 
                                         f32 %89 = OpLoad %35 
                                       f32_2 %90 = OpCompositeConstruct %89 %89 
                                       f32_2 %91 = OpFMul %88 %90 
                                       f32_2 %92 = OpLoad %12 
                                       f32_2 %93 = OpFAdd %91 %92 
                                       f32_4 %94 = OpLoad %9 
                                       f32_4 %95 = OpVectorShuffle %94 %93 4 5 2 3 
                                                     OpStore %9 %95 
                 read_only Texture2DSampled %102 = OpLoad %101 
                                      f32_4 %103 = OpLoad %9 
                                      f32_2 %104 = OpVectorShuffle %103 %103 0 1 
                                      f32_4 %105 = OpImageSampleImplicitLod %102 %104 
                                                     OpStore %97 %105 
                                                     OpReturn
                                                     OpFunctionEnd
"
}
}
Program "fp" {
SubProgram "d3d11 " {
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
""
}
SubProgram "vulkan " {
""
}
}
}
}
}