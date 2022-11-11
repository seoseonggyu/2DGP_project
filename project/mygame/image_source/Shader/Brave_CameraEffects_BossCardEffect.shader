//////////////////////////////////////////
//
// NOTE: This is *not* a valid shader file
//
///////////////////////////////////////////
Shader "Brave/CameraEffects/BossCardEffect" {
Properties {
_MainTex ("Base (RGB)", 2D) = "white" { }
_OverrideColor ("Fallback Color", Color) = (0,0,0,0)
}
SubShader {
 Pass {
  GpuProgramID 59703
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

uniform 	vec4 _OverrideColor;
uniform  sampler2D _MainTex;
in  vec2 vs_TEXCOORD0;
layout(location = 0) out vec4 SV_Target0;
vec4 u_xlat10_0;
vec4 u_xlat1;
void main()
{
    u_xlat10_0 = texture(_MainTex, vs_TEXCOORD0.xy);
    u_xlat1 = (-u_xlat10_0) + _OverrideColor;
    SV_Target0 = _OverrideColor.wwww * u_xlat1 + u_xlat10_0;
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
; Bound: 79
; Schema: 0
                                                    OpCapability Shader 
                                             %1 = OpExtInstImport "GLSL.std.450" 
                                                    OpMemoryModel Logical GLSL450 
                                                    OpEntryPoint Fragment %4 "main" %27 %70 
                                                    OpExecutionMode %4 OriginUpperLeft 
                                                    OpMemberDecorate %11 0 RelaxedPrecision 
                                                    OpMemberDecorate %11 0 Offset 11 
                                                    OpMemberDecorate %11 1 Offset 11 
                                                    OpDecorate %11 Block 
                                                    OpDecorate %13 DescriptorSet 13 
                                                    OpDecorate %13 Binding 13 
                                                    OpDecorate %20 RelaxedPrecision 
                                                    OpDecorate %25 RelaxedPrecision 
                                                    OpDecorate %27 RelaxedPrecision 
                                                    OpDecorate %27 Location 27 
                                                    OpDecorate %30 RelaxedPrecision 
                                                    OpDecorate %31 RelaxedPrecision 
                                                    OpDecorate %33 RelaxedPrecision 
                                                    OpDecorate %43 RelaxedPrecision 
                                                    OpDecorate %46 RelaxedPrecision 
                                                    OpDecorate %47 RelaxedPrecision 
                                                    OpDecorate %50 RelaxedPrecision 
                                                    OpDecorate %53 RelaxedPrecision 
                                                    OpDecorate %57 RelaxedPrecision 
                                                    OpDecorate %57 DescriptorSet 57 
                                                    OpDecorate %57 Binding 57 
                                                    OpDecorate %58 RelaxedPrecision 
                                                    OpDecorate %59 RelaxedPrecision 
                                                    OpDecorate %62 RelaxedPrecision 
                                                    OpDecorate %63 RelaxedPrecision 
                                                    OpDecorate %70 Location 70 
                                                    OpDecorate %76 RelaxedPrecision 
                                             %2 = OpTypeVoid 
                                             %3 = OpTypeFunction %2 
                                             %6 = OpTypeBool 
                                             %7 = OpTypePointer Private %6 
                               Private bool* %8 = OpVariable Private 
                                             %9 = OpTypeFloat 32 
                                            %10 = OpTypeVector %9 4 
                                            %11 = OpTypeStruct %10 %10 
                                            %12 = OpTypePointer Uniform %11 
            Uniform struct {f32_4; f32_4;}* %13 = OpVariable Uniform 
                                            %14 = OpTypeInt 32 1 
                                        i32 %15 = OpConstant 0 
                                            %16 = OpTypeInt 32 0 
                                        u32 %17 = OpConstant 1 
                                            %18 = OpTypePointer Uniform %9 
                                        f32 %21 = OpConstant 3.674022E-40 
                                            %23 = OpTypeVector %9 2 
                                            %24 = OpTypePointer Private %23 
                             Private f32_2* %25 = OpVariable Private 
                                            %26 = OpTypePointer Input %23 
                               Input f32_2* %27 = OpVariable Input 
                                            %28 = OpTypePointer Input %9 
                                        f32 %32 = OpConstant 3.674022E-40 
                                        u32 %34 = OpConstant 0 
                                            %35 = OpTypePointer Private %9 
                                            %37 = OpTypePointer Function %9 
                                            %52 = OpTypePointer Private %10 
                             Private f32_4* %53 = OpVariable Private 
                                            %54 = OpTypeImage %9 Dim2D 0 0 0 1 Unknown 
                                            %55 = OpTypeSampledImage %54 
                                            %56 = OpTypePointer UniformConstant %55 
UniformConstant read_only Texture2DSampled* %57 = OpVariable UniformConstant 
                             Private f32_4* %61 = OpVariable Private 
                                        i32 %64 = OpConstant 1 
                                            %65 = OpTypePointer Uniform %10 
                                            %69 = OpTypePointer Output %10 
                              Output f32_4* %70 = OpVariable Output 
                                        void %4 = OpFunction None %3 
                                             %5 = OpLabel 
                              Function f32* %38 = OpVariable Function 
                               Uniform f32* %19 = OpAccessChain %13 %15 %17 
                                        f32 %20 = OpLoad %19 
                                       bool %22 = OpFOrdLessThan %20 %21 
                                                    OpStore %8 %22 
                                 Input f32* %29 = OpAccessChain %27 %17 
                                        f32 %30 = OpLoad %29 
                                        f32 %31 = OpFNegate %30 
                                        f32 %33 = OpFAdd %31 %32 
                               Private f32* %36 = OpAccessChain %25 %34 
                                                    OpStore %36 %33 
                                       bool %39 = OpLoad %8 
                                                    OpSelectionMerge %41 None 
                                                    OpBranchConditional %39 %40 %44 
                                            %40 = OpLabel 
                               Private f32* %42 = OpAccessChain %25 %34 
                                        f32 %43 = OpLoad %42 
                                                    OpStore %38 %43 
                                                    OpBranch %41 
                                            %44 = OpLabel 
                                 Input f32* %45 = OpAccessChain %27 %17 
                                        f32 %46 = OpLoad %45 
                                                    OpStore %38 %46 
                                                    OpBranch %41 
                                            %41 = OpLabel 
                                        f32 %47 = OpLoad %38 
                               Private f32* %48 = OpAccessChain %25 %17 
                                                    OpStore %48 %47 
                                 Input f32* %49 = OpAccessChain %27 %34 
                                        f32 %50 = OpLoad %49 
                               Private f32* %51 = OpAccessChain %25 %34 
                                                    OpStore %51 %50 
                 read_only Texture2DSampled %58 = OpLoad %57 
                                      f32_2 %59 = OpLoad %25 
                                      f32_4 %60 = OpImageSampleImplicitLod %58 %59 
                                                    OpStore %53 %60 
                                      f32_4 %62 = OpLoad %53 
                                      f32_4 %63 = OpFNegate %62 
                             Uniform f32_4* %66 = OpAccessChain %13 %64 
                                      f32_4 %67 = OpLoad %66 
                                      f32_4 %68 = OpFAdd %63 %67 
                                                    OpStore %61 %68 
                             Uniform f32_4* %71 = OpAccessChain %13 %64 
                                      f32_4 %72 = OpLoad %71 
                                      f32_4 %73 = OpVectorShuffle %72 %72 3 3 3 3 
                                      f32_4 %74 = OpLoad %61 
                                      f32_4 %75 = OpFMul %73 %74 
                                      f32_4 %76 = OpLoad %53 
                                      f32_4 %77 = OpFAdd %75 %76 
                                                    OpStore %70 %77 
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