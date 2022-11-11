//////////////////////////////////////////
//
// NOTE: This is *not* a valid shader file
//
///////////////////////////////////////////
Shader "Particles/Additive" {
Properties {
_TintColor ("Tint Color", Color) = (0.5,0.5,0.5,0.5)
_MainTex ("Particle Texture", 2D) = "white" { }
_InvFade ("Soft Particles Factor", Range(0.01, 3)) = 1
}
SubShader {
 Tags { "IGNOREPROJECTOR" = "true" "PreviewType" = "Plane" "QUEUE" = "Transparent" "RenderType" = "Transparent" }
 Pass {
  Tags { "IGNOREPROJECTOR" = "true" "PreviewType" = "Plane" "QUEUE" = "Transparent" "RenderType" = "Transparent" }
  Blend SrcAlpha One, SrcAlpha One
  ColorMask RGB 0
  ZWrite Off
  Cull Off
  GpuProgramID 26823
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
uniform 	vec4 _MainTex_ST;
in  vec4 in_POSITION0;
in  vec4 in_COLOR0;
in  vec2 in_TEXCOORD0;
out vec4 vs_COLOR0;
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
    vs_COLOR0 = in_COLOR0;
    vs_TEXCOORD0.xy = in_TEXCOORD0.xy * _MainTex_ST.xy + _MainTex_ST.zw;
    return;
}

#endif
#ifdef FRAGMENT
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 _TintColor;
uniform  sampler2D _MainTex;
in  vec4 vs_COLOR0;
in  vec2 vs_TEXCOORD0;
layout(location = 0) out vec4 SV_Target0;
vec4 u_xlat0;
vec4 u_xlat10_1;
void main()
{
    u_xlat0 = vs_COLOR0 + vs_COLOR0;
    u_xlat0 = u_xlat0 * _TintColor;
    u_xlat10_1 = texture(_MainTex, vs_TEXCOORD0.xy);
    u_xlat0 = u_xlat0 * u_xlat10_1;
    SV_Target0.w = u_xlat0.w;
    SV_Target0.w = clamp(SV_Target0.w, 0.0, 1.0);
    SV_Target0.xyz = u_xlat0.xyz;
    return;
}

#endif
"
}
SubProgram "vulkan " {
"; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 105
; Schema: 0
                                                     OpCapability Shader 
                                              %1 = OpExtInstImport "GLSL.std.450" 
                                                     OpMemoryModel Logical GLSL450 
                                                     OpEntryPoint Vertex %4 "main" %11 %72 %82 %83 %87 %89 
                                                     OpDecorate %11 Location 11 
                                                     OpDecorate %16 ArrayStride 16 
                                                     OpDecorate %17 ArrayStride 17 
                                                     OpMemberDecorate %18 0 Offset 18 
                                                     OpMemberDecorate %18 1 Offset 18 
                                                     OpMemberDecorate %18 2 Offset 18 
                                                     OpDecorate %18 Block 
                                                     OpDecorate %20 DescriptorSet 20 
                                                     OpDecorate %20 Binding 20 
                                                     OpMemberDecorate %70 0 BuiltIn 70 
                                                     OpMemberDecorate %70 1 BuiltIn 70 
                                                     OpMemberDecorate %70 2 BuiltIn 70 
                                                     OpDecorate %70 Block 
                                                     OpDecorate %82 RelaxedPrecision 
                                                     OpDecorate %82 Location 82 
                                                     OpDecorate %83 RelaxedPrecision 
                                                     OpDecorate %83 Location 83 
                                                     OpDecorate %84 RelaxedPrecision 
                                                     OpDecorate %87 Location 87 
                                                     OpDecorate %89 Location 89 
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
                                             %18 = OpTypeStruct %16 %17 %7 
                                             %19 = OpTypePointer Uniform %18 
Uniform struct {f32_4[4]; f32_4[4]; f32_4;}* %20 = OpVariable Uniform 
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
                               Output f32_4* %82 = OpVariable Output 
                                Input f32_4* %83 = OpVariable Input 
                                             %85 = OpTypeVector %6 2 
                                             %86 = OpTypePointer Output %85 
                               Output f32_2* %87 = OpVariable Output 
                                             %88 = OpTypePointer Input %85 
                                Input f32_2* %89 = OpVariable Input 
                                             %99 = OpTypePointer Output %6 
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
                                       f32_4 %84 = OpLoad %83 
                                                     OpStore %82 %84 
                                       f32_2 %90 = OpLoad %89 
                              Uniform f32_4* %91 = OpAccessChain %20 %35 
                                       f32_4 %92 = OpLoad %91 
                                       f32_2 %93 = OpVectorShuffle %92 %92 0 1 
                                       f32_2 %94 = OpFMul %90 %93 
                              Uniform f32_4* %95 = OpAccessChain %20 %35 
                                       f32_4 %96 = OpLoad %95 
                                       f32_2 %97 = OpVectorShuffle %96 %96 2 3 
                                       f32_2 %98 = OpFAdd %94 %97 
                                                     OpStore %87 %98 
                                Output f32* %100 = OpAccessChain %72 %22 %68 
                                        f32 %101 = OpLoad %100 
                                        f32 %102 = OpFNegate %101 
                                Output f32* %103 = OpAccessChain %72 %22 %68 
                                                     OpStore %103 %102 
                                                     OpReturn
                                                     OpFunctionEnd
; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 60
; Schema: 0
                                                    OpCapability Shader 
                                             %1 = OpExtInstImport "GLSL.std.450" 
                                                    OpMemoryModel Logical GLSL450 
                                                    OpEntryPoint Fragment %4 "main" %11 %33 %40 
                                                    OpExecutionMode %4 OriginUpperLeft 
                                                    OpDecorate %9 RelaxedPrecision 
                                                    OpDecorate %11 RelaxedPrecision 
                                                    OpDecorate %11 Location 11 
                                                    OpDecorate %12 RelaxedPrecision 
                                                    OpDecorate %13 RelaxedPrecision 
                                                    OpDecorate %14 RelaxedPrecision 
                                                    OpDecorate %15 RelaxedPrecision 
                                                    OpMemberDecorate %16 0 RelaxedPrecision 
                                                    OpMemberDecorate %16 0 Offset 16 
                                                    OpDecorate %16 Block 
                                                    OpDecorate %18 DescriptorSet 18 
                                                    OpDecorate %18 Binding 18 
                                                    OpDecorate %23 RelaxedPrecision 
                                                    OpDecorate %24 RelaxedPrecision 
                                                    OpDecorate %25 RelaxedPrecision 
                                                    OpDecorate %29 RelaxedPrecision 
                                                    OpDecorate %29 DescriptorSet 29 
                                                    OpDecorate %29 Binding 29 
                                                    OpDecorate %30 RelaxedPrecision 
                                                    OpDecorate %33 Location 33 
                                                    OpDecorate %36 RelaxedPrecision 
                                                    OpDecorate %37 RelaxedPrecision 
                                                    OpDecorate %38 RelaxedPrecision 
                                                    OpDecorate %40 RelaxedPrecision 
                                                    OpDecorate %40 Location 40 
                                                    OpDecorate %45 RelaxedPrecision 
                                                    OpDecorate %49 RelaxedPrecision 
                                                    OpDecorate %52 RelaxedPrecision 
                                                    OpDecorate %55 RelaxedPrecision 
                                                    OpDecorate %56 RelaxedPrecision 
                                             %2 = OpTypeVoid 
                                             %3 = OpTypeFunction %2 
                                             %6 = OpTypeFloat 32 
                                             %7 = OpTypeVector %6 4 
                                             %8 = OpTypePointer Private %7 
                              Private f32_4* %9 = OpVariable Private 
                                            %10 = OpTypePointer Input %7 
                               Input f32_4* %11 = OpVariable Input 
                                            %16 = OpTypeStruct %7 
                                            %17 = OpTypePointer Uniform %16 
                   Uniform struct {f32_4;}* %18 = OpVariable Uniform 
                                            %19 = OpTypeInt 32 1 
                                        i32 %20 = OpConstant 0 
                                            %21 = OpTypePointer Uniform %7 
                             Private f32_4* %25 = OpVariable Private 
                                            %26 = OpTypeImage %6 Dim2D 0 0 0 1 Unknown 
                                            %27 = OpTypeSampledImage %26 
                                            %28 = OpTypePointer UniformConstant %27 
UniformConstant read_only Texture2DSampled* %29 = OpVariable UniformConstant 
                                            %31 = OpTypeVector %6 2 
                                            %32 = OpTypePointer Input %31 
                               Input f32_2* %33 = OpVariable Input 
                                            %39 = OpTypePointer Output %7 
                              Output f32_4* %40 = OpVariable Output 
                                            %41 = OpTypeInt 32 0 
                                        u32 %42 = OpConstant 3 
                                            %43 = OpTypePointer Private %6 
                                            %46 = OpTypePointer Output %6 
                                        f32 %50 = OpConstant 3.674022E-40 
                                        f32 %51 = OpConstant 3.674022E-40 
                                            %54 = OpTypeVector %6 3 
                                        void %4 = OpFunction None %3 
                                             %5 = OpLabel 
                                      f32_4 %12 = OpLoad %11 
                                      f32_4 %13 = OpLoad %11 
                                      f32_4 %14 = OpFAdd %12 %13 
                                                    OpStore %9 %14 
                                      f32_4 %15 = OpLoad %9 
                             Uniform f32_4* %22 = OpAccessChain %18 %20 
                                      f32_4 %23 = OpLoad %22 
                                      f32_4 %24 = OpFMul %15 %23 
                                                    OpStore %9 %24 
                 read_only Texture2DSampled %30 = OpLoad %29 
                                      f32_2 %34 = OpLoad %33 
                                      f32_4 %35 = OpImageSampleImplicitLod %30 %34 
                                                    OpStore %25 %35 
                                      f32_4 %36 = OpLoad %9 
                                      f32_4 %37 = OpLoad %25 
                                      f32_4 %38 = OpFMul %36 %37 
                                                    OpStore %9 %38 
                               Private f32* %44 = OpAccessChain %9 %42 
                                        f32 %45 = OpLoad %44 
                                Output f32* %47 = OpAccessChain %40 %42 
                                                    OpStore %47 %45 
                                Output f32* %48 = OpAccessChain %40 %42 
                                        f32 %49 = OpLoad %48 
                                        f32 %52 = OpExtInst %1 43 %49 %50 %51 
                                Output f32* %53 = OpAccessChain %40 %42 
                                                    OpStore %53 %52 
                                      f32_4 %55 = OpLoad %9 
                                      f32_3 %56 = OpVectorShuffle %55 %55 0 1 2 
                                      f32_4 %57 = OpLoad %40 
                                      f32_4 %58 = OpVectorShuffle %57 %56 4 5 6 3 
                                                    OpStore %40 %58 
                                                    OpReturn
                                                    OpFunctionEnd
"
}
SubProgram "d3d11 " {
Keywords { "SOFTPARTICLES_ON" }
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
Keywords { "SOFTPARTICLES_ON" }
"#ifdef VERTEX
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 _ProjectionParams;
uniform 	vec4 hlslcc_mtx4x4unity_ObjectToWorld[4];
uniform 	vec4 hlslcc_mtx4x4unity_MatrixV[4];
uniform 	vec4 hlslcc_mtx4x4unity_MatrixVP[4];
uniform 	vec4 _MainTex_ST;
in  vec4 in_POSITION0;
in  vec4 in_COLOR0;
in  vec2 in_TEXCOORD0;
out vec4 vs_COLOR0;
out vec2 vs_TEXCOORD0;
out vec4 vs_TEXCOORD2;
vec4 u_xlat0;
vec4 u_xlat1;
float u_xlat2;
void main()
{
    u_xlat0 = in_POSITION0.yyyy * hlslcc_mtx4x4unity_ObjectToWorld[1];
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[0] * in_POSITION0.xxxx + u_xlat0;
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[2] * in_POSITION0.zzzz + u_xlat0;
    u_xlat0 = u_xlat0 + hlslcc_mtx4x4unity_ObjectToWorld[3];
    u_xlat1 = u_xlat0.yyyy * hlslcc_mtx4x4unity_MatrixVP[1];
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[0] * u_xlat0.xxxx + u_xlat1;
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[2] * u_xlat0.zzzz + u_xlat1;
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[3] * u_xlat0.wwww + u_xlat1;
    gl_Position = u_xlat1;
    vs_COLOR0 = in_COLOR0;
    vs_TEXCOORD0.xy = in_TEXCOORD0.xy * _MainTex_ST.xy + _MainTex_ST.zw;
    u_xlat2 = u_xlat0.y * hlslcc_mtx4x4unity_MatrixV[1].z;
    u_xlat0.x = hlslcc_mtx4x4unity_MatrixV[0].z * u_xlat0.x + u_xlat2;
    u_xlat0.x = hlslcc_mtx4x4unity_MatrixV[2].z * u_xlat0.z + u_xlat0.x;
    u_xlat0.x = hlslcc_mtx4x4unity_MatrixV[3].z * u_xlat0.w + u_xlat0.x;
    vs_TEXCOORD2.z = (-u_xlat0.x);
    u_xlat0.x = u_xlat1.y * _ProjectionParams.x;
    u_xlat0.w = u_xlat0.x * 0.5;
    u_xlat0.xz = u_xlat1.xw * vec2(0.5, 0.5);
    vs_TEXCOORD2.w = u_xlat1.w;
    vs_TEXCOORD2.xy = u_xlat0.zz + u_xlat0.xw;
    return;
}

#endif
#ifdef FRAGMENT
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 _ZBufferParams;
uniform 	vec4 _TintColor;
uniform 	float _InvFade;
uniform  sampler2D _CameraDepthTexture;
uniform  sampler2D _MainTex;
in  vec4 vs_COLOR0;
in  vec2 vs_TEXCOORD0;
in  vec4 vs_TEXCOORD2;
layout(location = 0) out vec4 SV_Target0;
vec4 u_xlat0;
vec4 u_xlat10_0;
vec4 u_xlat10_1;
void main()
{
    u_xlat0.xy = vs_TEXCOORD2.xy / vs_TEXCOORD2.ww;
    u_xlat10_0 = texture(_CameraDepthTexture, u_xlat0.xy);
    u_xlat0.x = _ZBufferParams.z * u_xlat10_0.x + _ZBufferParams.w;
    u_xlat0.x = float(1.0) / u_xlat0.x;
    u_xlat0.x = u_xlat0.x + (-vs_TEXCOORD2.z);
    u_xlat0.x = u_xlat0.x * _InvFade;
    u_xlat0.x = clamp(u_xlat0.x, 0.0, 1.0);
    u_xlat0.w = u_xlat0.x * vs_COLOR0.w;
    u_xlat0.xyz = vs_COLOR0.xyz;
    u_xlat0 = u_xlat0 + u_xlat0;
    u_xlat0 = u_xlat0 * _TintColor;
    u_xlat10_1 = texture(_MainTex, vs_TEXCOORD0.xy);
    u_xlat0 = u_xlat0 * u_xlat10_1;
    SV_Target0.w = u_xlat0.w;
    SV_Target0.w = clamp(SV_Target0.w, 0.0, 1.0);
    SV_Target0.xyz = u_xlat0.xyz;
    return;
}

#endif
"
}
SubProgram "vulkan " {
Keywords { "SOFTPARTICLES_ON" }
"; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 177
; Schema: 0
                                                      OpCapability Shader 
                                               %1 = OpExtInstImport "GLSL.std.450" 
                                                      OpMemoryModel Logical GLSL450 
                                                      OpEntryPoint Vertex %4 "main" %11 %80 %84 %85 %89 %91 %139 
                                                      OpDecorate %11 Location 11 
                                                      OpDecorate %16 ArrayStride 16 
                                                      OpDecorate %17 ArrayStride 17 
                                                      OpDecorate %18 ArrayStride 18 
                                                      OpMemberDecorate %19 0 Offset 19 
                                                      OpMemberDecorate %19 1 Offset 19 
                                                      OpMemberDecorate %19 2 Offset 19 
                                                      OpMemberDecorate %19 3 Offset 19 
                                                      OpMemberDecorate %19 4 Offset 19 
                                                      OpDecorate %19 Block 
                                                      OpDecorate %21 DescriptorSet 21 
                                                      OpDecorate %21 Binding 21 
                                                      OpMemberDecorate %78 0 BuiltIn 78 
                                                      OpMemberDecorate %78 1 BuiltIn 78 
                                                      OpMemberDecorate %78 2 BuiltIn 78 
                                                      OpDecorate %78 Block 
                                                      OpDecorate %84 RelaxedPrecision 
                                                      OpDecorate %84 Location 84 
                                                      OpDecorate %85 RelaxedPrecision 
                                                      OpDecorate %85 Location 85 
                                                      OpDecorate %86 RelaxedPrecision 
                                                      OpDecorate %89 Location 89 
                                                      OpDecorate %91 Location 91 
                                                      OpDecorate %139 Location 139 
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
                                              %18 = OpTypeArray %7 %15 
                                              %19 = OpTypeStruct %7 %16 %17 %18 %7 
                                              %20 = OpTypePointer Uniform %19 
Uniform struct {f32_4; f32_4[4]; f32_4[4]; f32_4[4]; f32_4;}* %21 = OpVariable Uniform 
                                              %22 = OpTypeInt 32 1 
                                          i32 %23 = OpConstant 1 
                                              %24 = OpTypePointer Uniform %7 
                                          i32 %28 = OpConstant 0 
                                          i32 %36 = OpConstant 2 
                                          i32 %45 = OpConstant 3 
                               Private f32_4* %49 = OpVariable Private 
                                          u32 %76 = OpConstant 1 
                                              %77 = OpTypeArray %6 %76 
                                              %78 = OpTypeStruct %7 %6 %77 
                                              %79 = OpTypePointer Output %78 
         Output struct {f32_4; f32; f32[1];}* %80 = OpVariable Output 
                                              %82 = OpTypePointer Output %7 
                                Output f32_4* %84 = OpVariable Output 
                                 Input f32_4* %85 = OpVariable Input 
                                              %87 = OpTypeVector %6 2 
                                              %88 = OpTypePointer Output %87 
                                Output f32_2* %89 = OpVariable Output 
                                              %90 = OpTypePointer Input %87 
                                 Input f32_2* %91 = OpVariable Input 
                                          i32 %93 = OpConstant 4 
                                             %102 = OpTypePointer Private %6 
                                Private f32* %103 = OpVariable Private 
                                         u32 %106 = OpConstant 2 
                                             %107 = OpTypePointer Uniform %6 
                                         u32 %113 = OpConstant 0 
                                         u32 %131 = OpConstant 3 
                               Output f32_4* %139 = OpVariable Output 
                                             %143 = OpTypePointer Output %6 
                                         f32 %153 = OpConstant 3.674022E-40 
                                       f32_2 %158 = OpConstantComposite %153 %153 
                                          void %4 = OpFunction None %3 
                                               %5 = OpLabel 
                                        f32_4 %12 = OpLoad %11 
                                        f32_4 %13 = OpVectorShuffle %12 %12 1 1 1 1 
                               Uniform f32_4* %25 = OpAccessChain %21 %23 %23 
                                        f32_4 %26 = OpLoad %25 
                                        f32_4 %27 = OpFMul %13 %26 
                                                      OpStore %9 %27 
                               Uniform f32_4* %29 = OpAccessChain %21 %23 %28 
                                        f32_4 %30 = OpLoad %29 
                                        f32_4 %31 = OpLoad %11 
                                        f32_4 %32 = OpVectorShuffle %31 %31 0 0 0 0 
                                        f32_4 %33 = OpFMul %30 %32 
                                        f32_4 %34 = OpLoad %9 
                                        f32_4 %35 = OpFAdd %33 %34 
                                                      OpStore %9 %35 
                               Uniform f32_4* %37 = OpAccessChain %21 %23 %36 
                                        f32_4 %38 = OpLoad %37 
                                        f32_4 %39 = OpLoad %11 
                                        f32_4 %40 = OpVectorShuffle %39 %39 2 2 2 2 
                                        f32_4 %41 = OpFMul %38 %40 
                                        f32_4 %42 = OpLoad %9 
                                        f32_4 %43 = OpFAdd %41 %42 
                                                      OpStore %9 %43 
                                        f32_4 %44 = OpLoad %9 
                               Uniform f32_4* %46 = OpAccessChain %21 %23 %45 
                                        f32_4 %47 = OpLoad %46 
                                        f32_4 %48 = OpFAdd %44 %47 
                                                      OpStore %9 %48 
                                        f32_4 %50 = OpLoad %9 
                                        f32_4 %51 = OpVectorShuffle %50 %50 1 1 1 1 
                               Uniform f32_4* %52 = OpAccessChain %21 %45 %23 
                                        f32_4 %53 = OpLoad %52 
                                        f32_4 %54 = OpFMul %51 %53 
                                                      OpStore %49 %54 
                               Uniform f32_4* %55 = OpAccessChain %21 %45 %28 
                                        f32_4 %56 = OpLoad %55 
                                        f32_4 %57 = OpLoad %9 
                                        f32_4 %58 = OpVectorShuffle %57 %57 0 0 0 0 
                                        f32_4 %59 = OpFMul %56 %58 
                                        f32_4 %60 = OpLoad %49 
                                        f32_4 %61 = OpFAdd %59 %60 
                                                      OpStore %49 %61 
                               Uniform f32_4* %62 = OpAccessChain %21 %45 %36 
                                        f32_4 %63 = OpLoad %62 
                                        f32_4 %64 = OpLoad %9 
                                        f32_4 %65 = OpVectorShuffle %64 %64 2 2 2 2 
                                        f32_4 %66 = OpFMul %63 %65 
                                        f32_4 %67 = OpLoad %49 
                                        f32_4 %68 = OpFAdd %66 %67 
                                                      OpStore %49 %68 
                               Uniform f32_4* %69 = OpAccessChain %21 %45 %45 
                                        f32_4 %70 = OpLoad %69 
                                        f32_4 %71 = OpLoad %9 
                                        f32_4 %72 = OpVectorShuffle %71 %71 3 3 3 3 
                                        f32_4 %73 = OpFMul %70 %72 
                                        f32_4 %74 = OpLoad %49 
                                        f32_4 %75 = OpFAdd %73 %74 
                                                      OpStore %49 %75 
                                        f32_4 %81 = OpLoad %49 
                                Output f32_4* %83 = OpAccessChain %80 %28 
                                                      OpStore %83 %81 
                                        f32_4 %86 = OpLoad %85 
                                                      OpStore %84 %86 
                                        f32_2 %92 = OpLoad %91 
                               Uniform f32_4* %94 = OpAccessChain %21 %93 
                                        f32_4 %95 = OpLoad %94 
                                        f32_2 %96 = OpVectorShuffle %95 %95 0 1 
                                        f32_2 %97 = OpFMul %92 %96 
                               Uniform f32_4* %98 = OpAccessChain %21 %93 
                                        f32_4 %99 = OpLoad %98 
                                       f32_2 %100 = OpVectorShuffle %99 %99 2 3 
                                       f32_2 %101 = OpFAdd %97 %100 
                                                      OpStore %89 %101 
                                Private f32* %104 = OpAccessChain %9 %76 
                                         f32 %105 = OpLoad %104 
                                Uniform f32* %108 = OpAccessChain %21 %36 %23 %106 
                                         f32 %109 = OpLoad %108 
                                         f32 %110 = OpFMul %105 %109 
                                                      OpStore %103 %110 
                                Uniform f32* %111 = OpAccessChain %21 %36 %28 %106 
                                         f32 %112 = OpLoad %111 
                                Private f32* %114 = OpAccessChain %9 %113 
                                         f32 %115 = OpLoad %114 
                                         f32 %116 = OpFMul %112 %115 
                                         f32 %117 = OpLoad %103 
                                         f32 %118 = OpFAdd %116 %117 
                                Private f32* %119 = OpAccessChain %9 %113 
                                                      OpStore %119 %118 
                                Uniform f32* %120 = OpAccessChain %21 %36 %36 %106 
                                         f32 %121 = OpLoad %120 
                                Private f32* %122 = OpAccessChain %9 %106 
                                         f32 %123 = OpLoad %122 
                                         f32 %124 = OpFMul %121 %123 
                                Private f32* %125 = OpAccessChain %9 %113 
                                         f32 %126 = OpLoad %125 
                                         f32 %127 = OpFAdd %124 %126 
                                Private f32* %128 = OpAccessChain %9 %113 
                                                      OpStore %128 %127 
                                Uniform f32* %129 = OpAccessChain %21 %36 %45 %106 
                                         f32 %130 = OpLoad %129 
                                Private f32* %132 = OpAccessChain %9 %131 
                                         f32 %133 = OpLoad %132 
                                         f32 %134 = OpFMul %130 %133 
                                Private f32* %135 = OpAccessChain %9 %113 
                                         f32 %136 = OpLoad %135 
                                         f32 %137 = OpFAdd %134 %136 
                                Private f32* %138 = OpAccessChain %9 %113 
                                                      OpStore %138 %137 
                                Private f32* %140 = OpAccessChain %9 %113 
                                         f32 %141 = OpLoad %140 
                                         f32 %142 = OpFNegate %141 
                                 Output f32* %144 = OpAccessChain %139 %106 
                                                      OpStore %144 %142 
                                Private f32* %145 = OpAccessChain %49 %76 
                                         f32 %146 = OpLoad %145 
                                Uniform f32* %147 = OpAccessChain %21 %28 %113 
                                         f32 %148 = OpLoad %147 
                                         f32 %149 = OpFMul %146 %148 
                                Private f32* %150 = OpAccessChain %9 %113 
                                                      OpStore %150 %149 
                                Private f32* %151 = OpAccessChain %9 %113 
                                         f32 %152 = OpLoad %151 
                                         f32 %154 = OpFMul %152 %153 
                                Private f32* %155 = OpAccessChain %9 %131 
                                                      OpStore %155 %154 
                                       f32_4 %156 = OpLoad %49 
                                       f32_2 %157 = OpVectorShuffle %156 %156 0 3 
                                       f32_2 %159 = OpFMul %157 %158 
                                       f32_4 %160 = OpLoad %9 
                                       f32_4 %161 = OpVectorShuffle %160 %159 4 1 5 3 
                                                      OpStore %9 %161 
                                Private f32* %162 = OpAccessChain %49 %131 
                                         f32 %163 = OpLoad %162 
                                 Output f32* %164 = OpAccessChain %139 %131 
                                                      OpStore %164 %163 
                                       f32_4 %165 = OpLoad %9 
                                       f32_2 %166 = OpVectorShuffle %165 %165 2 2 
                                       f32_4 %167 = OpLoad %9 
                                       f32_2 %168 = OpVectorShuffle %167 %167 0 3 
                                       f32_2 %169 = OpFAdd %166 %168 
                                       f32_4 %170 = OpLoad %139 
                                       f32_4 %171 = OpVectorShuffle %170 %169 4 5 2 3 
                                                      OpStore %139 %171 
                                 Output f32* %172 = OpAccessChain %80 %28 %76 
                                         f32 %173 = OpLoad %172 
                                         f32 %174 = OpFNegate %173 
                                 Output f32* %175 = OpAccessChain %80 %28 %76 
                                                      OpStore %175 %174 
                                                      OpReturn
                                                      OpFunctionEnd
; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 121
; Schema: 0
                                                    OpCapability Shader 
                                             %1 = OpExtInstImport "GLSL.std.450" 
                                                    OpMemoryModel Logical GLSL450 
                                                    OpEntryPoint Fragment %4 "main" %11 %75 %100 %107 
                                                    OpExecutionMode %4 OriginUpperLeft 
                                                    OpDecorate %11 Location 11 
                                                    OpDecorate %23 DescriptorSet 23 
                                                    OpDecorate %23 Binding 23 
                                                    OpMemberDecorate %33 0 Offset 33 
                                                    OpMemberDecorate %33 1 RelaxedPrecision 
                                                    OpMemberDecorate %33 1 Offset 33 
                                                    OpMemberDecorate %33 2 Offset 33 
                                                    OpDecorate %33 Block 
                                                    OpDecorate %35 DescriptorSet 35 
                                                    OpDecorate %35 Binding 35 
                                                    OpDecorate %75 RelaxedPrecision 
                                                    OpDecorate %75 Location 75 
                                                    OpDecorate %76 RelaxedPrecision 
                                                    OpDecorate %77 RelaxedPrecision 
                                                    OpDecorate %83 RelaxedPrecision 
                                                    OpDecorate %84 RelaxedPrecision 
                                                    OpDecorate %85 RelaxedPrecision 
                                                    OpDecorate %86 RelaxedPrecision 
                                                    OpDecorate %87 RelaxedPrecision 
                                                    OpDecorate %94 RelaxedPrecision 
                                                    OpDecorate %96 RelaxedPrecision 
                                                    OpDecorate %97 RelaxedPrecision 
                                                    OpDecorate %97 DescriptorSet 97 
                                                    OpDecorate %97 Binding 97 
                                                    OpDecorate %98 RelaxedPrecision 
                                                    OpDecorate %100 Location 100 
                                                    OpDecorate %104 RelaxedPrecision 
                                                    OpDecorate %107 RelaxedPrecision 
                                                    OpDecorate %107 Location 107 
                                                    OpDecorate %113 RelaxedPrecision 
                                                    OpDecorate %114 RelaxedPrecision 
                                             %2 = OpTypeVoid 
                                             %3 = OpTypeFunction %2 
                                             %6 = OpTypeFloat 32 
                                             %7 = OpTypeVector %6 4 
                                             %8 = OpTypePointer Private %7 
                              Private f32_4* %9 = OpVariable Private 
                                            %10 = OpTypePointer Input %7 
                               Input f32_4* %11 = OpVariable Input 
                                            %12 = OpTypeVector %6 2 
                                            %20 = OpTypeImage %6 Dim2D 0 0 0 1 Unknown 
                                            %21 = OpTypeSampledImage %20 
                                            %22 = OpTypePointer UniformConstant %21 
UniformConstant read_only Texture2DSampled* %23 = OpVariable UniformConstant 
                                            %28 = OpTypeInt 32 0 
                                        u32 %29 = OpConstant 0 
                                            %31 = OpTypePointer Private %6 
                                            %33 = OpTypeStruct %7 %7 %6 
                                            %34 = OpTypePointer Uniform %33 
       Uniform struct {f32_4; f32_4; f32;}* %35 = OpVariable Uniform 
                                            %36 = OpTypeInt 32 1 
                                        i32 %37 = OpConstant 0 
                                        u32 %38 = OpConstant 2 
                                            %39 = OpTypePointer Uniform %6 
                                        u32 %45 = OpConstant 3 
                                        f32 %50 = OpConstant 3.674022E-40 
                                            %57 = OpTypePointer Input %6 
                                        i32 %65 = OpConstant 2 
                                        f32 %72 = OpConstant 3.674022E-40 
                               Input f32_4* %75 = OpVariable Input 
                                            %82 = OpTypeVector %6 3 
                                        i32 %91 = OpConstant 1 
                                            %92 = OpTypePointer Uniform %7 
                             Private f32_4* %96 = OpVariable Private 
UniformConstant read_only Texture2DSampled* %97 = OpVariable UniformConstant 
                                            %99 = OpTypePointer Input %12 
                              Input f32_2* %100 = OpVariable Input 
                                           %106 = OpTypePointer Output %7 
                             Output f32_4* %107 = OpVariable Output 
                                           %110 = OpTypePointer Output %6 
                                        void %4 = OpFunction None %3 
                                             %5 = OpLabel 
                                      f32_4 %13 = OpLoad %11 
                                      f32_2 %14 = OpVectorShuffle %13 %13 0 1 
                                      f32_4 %15 = OpLoad %11 
                                      f32_2 %16 = OpVectorShuffle %15 %15 3 3 
                                      f32_2 %17 = OpFDiv %14 %16 
                                      f32_4 %18 = OpLoad %9 
                                      f32_4 %19 = OpVectorShuffle %18 %17 4 5 2 3 
                                                    OpStore %9 %19 
                 read_only Texture2DSampled %24 = OpLoad %23 
                                      f32_4 %25 = OpLoad %9 
                                      f32_2 %26 = OpVectorShuffle %25 %25 0 1 
                                      f32_4 %27 = OpImageSampleImplicitLod %24 %26 
                                        f32 %30 = OpCompositeExtract %27 0 
                               Private f32* %32 = OpAccessChain %9 %29 
                                                    OpStore %32 %30 
                               Uniform f32* %40 = OpAccessChain %35 %37 %38 
                                        f32 %41 = OpLoad %40 
                               Private f32* %42 = OpAccessChain %9 %29 
                                        f32 %43 = OpLoad %42 
                                        f32 %44 = OpFMul %41 %43 
                               Uniform f32* %46 = OpAccessChain %35 %37 %45 
                                        f32 %47 = OpLoad %46 
                                        f32 %48 = OpFAdd %44 %47 
                               Private f32* %49 = OpAccessChain %9 %29 
                                                    OpStore %49 %48 
                               Private f32* %51 = OpAccessChain %9 %29 
                                        f32 %52 = OpLoad %51 
                                        f32 %53 = OpFDiv %50 %52 
                               Private f32* %54 = OpAccessChain %9 %29 
                                                    OpStore %54 %53 
                               Private f32* %55 = OpAccessChain %9 %29 
                                        f32 %56 = OpLoad %55 
                                 Input f32* %58 = OpAccessChain %11 %38 
                                        f32 %59 = OpLoad %58 
                                        f32 %60 = OpFNegate %59 
                                        f32 %61 = OpFAdd %56 %60 
                               Private f32* %62 = OpAccessChain %9 %29 
                                                    OpStore %62 %61 
                               Private f32* %63 = OpAccessChain %9 %29 
                                        f32 %64 = OpLoad %63 
                               Uniform f32* %66 = OpAccessChain %35 %65 
                                        f32 %67 = OpLoad %66 
                                        f32 %68 = OpFMul %64 %67 
                               Private f32* %69 = OpAccessChain %9 %29 
                                                    OpStore %69 %68 
                               Private f32* %70 = OpAccessChain %9 %29 
                                        f32 %71 = OpLoad %70 
                                        f32 %73 = OpExtInst %1 43 %71 %72 %50 
                               Private f32* %74 = OpAccessChain %9 %29 
                                                    OpStore %74 %73 
                                      f32_4 %76 = OpLoad %75 
                                      f32_2 %77 = OpVectorShuffle %76 %76 3 3 
                                      f32_4 %78 = OpLoad %9 
                                      f32_2 %79 = OpVectorShuffle %78 %78 0 0 
                                        f32 %80 = OpDot %77 %79 
                               Private f32* %81 = OpAccessChain %9 %45 
                                                    OpStore %81 %80 
                                      f32_4 %83 = OpLoad %75 
                                      f32_3 %84 = OpVectorShuffle %83 %83 0 1 2 
                                      f32_4 %85 = OpLoad %75 
                                      f32_3 %86 = OpVectorShuffle %85 %85 0 1 2 
                                      f32_3 %87 = OpFAdd %84 %86 
                                      f32_4 %88 = OpLoad %9 
                                      f32_4 %89 = OpVectorShuffle %88 %87 4 5 6 3 
                                                    OpStore %9 %89 
                                      f32_4 %90 = OpLoad %9 
                             Uniform f32_4* %93 = OpAccessChain %35 %91 
                                      f32_4 %94 = OpLoad %93 
                                      f32_4 %95 = OpFMul %90 %94 
                                                    OpStore %9 %95 
                 read_only Texture2DSampled %98 = OpLoad %97 
                                     f32_2 %101 = OpLoad %100 
                                     f32_4 %102 = OpImageSampleImplicitLod %98 %101 
                                                    OpStore %96 %102 
                                     f32_4 %103 = OpLoad %9 
                                     f32_4 %104 = OpLoad %96 
                                     f32_4 %105 = OpFMul %103 %104 
                                                    OpStore %9 %105 
                              Private f32* %108 = OpAccessChain %9 %45 
                                       f32 %109 = OpLoad %108 
                               Output f32* %111 = OpAccessChain %107 %45 
                                                    OpStore %111 %109 
                               Output f32* %112 = OpAccessChain %107 %45 
                                       f32 %113 = OpLoad %112 
                                       f32 %114 = OpExtInst %1 43 %113 %72 %50 
                               Output f32* %115 = OpAccessChain %107 %45 
                                                    OpStore %115 %114 
                                     f32_4 %116 = OpLoad %9 
                                     f32_3 %117 = OpVectorShuffle %116 %116 0 1 2 
                                     f32_4 %118 = OpLoad %107 
                                     f32_4 %119 = OpVectorShuffle %118 %117 4 5 6 3 
                                                    OpStore %107 %119 
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
SubProgram "d3d11 " {
Keywords { "SOFTPARTICLES_ON" }
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
Keywords { "SOFTPARTICLES_ON" }
""
}
SubProgram "vulkan " {
Keywords { "SOFTPARTICLES_ON" }
""
}
}
}
}
}